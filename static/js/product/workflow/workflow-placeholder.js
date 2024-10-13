function setupPlaceholderInput(identifier, placeholderText) {
  let quill = new Quill('#' + identifier, {
    theme: 'snow',
    formats: [
      identifier
    ],
    modules: {
      toolbar: false,
      keyboard: {
        bindings: {
          custom_backspace: {
            key: 'Backspace',
            handler: function(range, context) {
              if (range.index === 0) return true;

              let [prevBlot, offset] = quill.getLeaf(range.index - 1);
              if (prevBlot instanceof PlaceholderBlot) {
                quill.deleteText(range.index - 1, 1, Quill.sources.USER);
                return false;
              }

              let length = quill.getLength();
              let lastLine = quill.getLine(length - 2)[0];
              if (range.index >= length - 1 && lastLine && lastLine.domNode.innerText.trim() === "") {
                quill.deleteText(range.index - 1, 1, Quill.sources.USER);
                return false;
              }
              return true;
            }
          },
          custom_delete: {
            key: 'Delete',
            handler: function(range, context) {
              let [nextBlot, offset] = quill.getLeaf(range.index);
              if (nextBlot instanceof PlaceholderBlot) {
                quill.deleteText(range.index, 1, Quill.sources.USER);
                return false;
              }

              let length = quill.getLength();
              let lastLine = quill.getLine(length - 2)[0];

              if (range.index === length - 1 && lastLine && lastLine.domNode.innerText.trim() === "") {
                quill.deleteText(range.index - 1, 1, Quill.sources.USER);
                return false;
              }
              return true;
            }
          },
          custom_left: {
            key: 'ArrowLeft',
            handler: function(range, context) {
              if (range.index === 0) return true;

              let [prevBlot, offset] = quill.getLeaf(range.index - 1);
              if (prevBlot instanceof PlaceholderBlot) {
                quill.setSelection(range.index - 1, 0, Quill.sources.USER);
                return false;
              }
              return true;
            }
          },
          custom_right: {
            key: 'ArrowRight',
            handler: function(range, context) {
              let [nextBlot, offset] = quill.getLeaf(range.index);
              if (nextBlot instanceof PlaceholderBlot) {
                quill.setSelection(range.index + 1, 0, Quill.sources.USER);
                return false;
              }
              return true;
            }
          }
        }
      }
    }
  });

  var Embed = Quill.import('blots/embed');
  class PlaceholderBlot extends Embed {
    static create(value) {
      let node = super.create();
      node.classList.add('placeholder');
      node.setAttribute('data-placeholder', value);
      node.innerText = value;
      return node;
    }

    static value(node) {
      return node.getAttribute('data-placeholder');
    }
  }
  PlaceholderBlot.blotName = identifier;
  PlaceholderBlot.tagName = 'span';
  if (!Quill.imports['formats/' + identifier]) {
    Quill.register(PlaceholderBlot);
  }

  const placeholder = document.createElement('div');
  placeholder.classList.add('quill-placeholder');
  placeholder.textContent = placeholderText;
  quill.container.appendChild(placeholder);

  quill.on('text-change', function(delta, oldDelta, source) {
    removeTrailingEmptyParagraphs(quill);
    adjustEditorHeight(quill);
    updatePlaceholderVisibility(quill, placeholder);
  });

  quill.container.addEventListener('click', function(event) {
    const range = quill.getSelection();
    if (range) {
      let [blot, offset] = quill.getLeaf(range.index);
      const cursorPosition = range.index;
      if (blot.domNode.nodeType === Node.TEXT_NODE && offset === blot.length()) {
        let nextBlot = blot.next;
        let placeholderCount = 0;
        while (nextBlot instanceof PlaceholderBlot) {
          placeholderCount++;
          nextBlot = nextBlot.next;
          if (!nextBlot || !(nextBlot instanceof PlaceholderBlot)) {
            break;
          }
        }
        if (placeholderCount > 0 && (!nextBlot || !(nextBlot instanceof PlaceholderBlot))) {
          quill.setSelection(cursorPosition + placeholderCount, Quill.sources.USER);
          event.preventDefault();
        }
      }
    }
  });

  removeTrailingEmptyParagraphs(quill);
  adjustEditorHeight(quill);
  updatePlaceholderVisibility(quill, placeholder);

  return quill;
}

function removeTrailingEmptyParagraphs(quill) {
  const length = quill.getLength();
  const [lastBlot, offset] = quill.getLeaf(length - 2);
  if (lastBlot && lastBlot.domNode.nodeType === Node.ELEMENT_NODE && lastBlot.domNode.tagName === 'P' && lastBlot.domNode.innerHTML === '<br>') {
    quill.deleteText(length - 2, 1, Quill.sources.SILENT);
  }
}

function adjustEditorHeight(quill) {
  const editor = quill.container.querySelector('.ql-editor');
  const container = quill.container;
  editor.style.height = 'auto';
  const newHeight = Math.max(editor.scrollHeight + 14, 37) + 'px';
  container.style.height = newHeight;
  editor.style.height = newHeight;
}

function updatePlaceholderVisibility(quill, placeholder) {
  const isEmpty = quill.getLength() <= 1;
  placeholder.style.opacity = isEmpty ? '1' : '0';
}

function addPlaceholder(quill, identifier, name) {
  var range = quill.getSelection(true);
  if (range) {
    quill.insertEmbed(range.index, identifier, ' ' + name + ' ', Quill.sources.USER);
    quill.setSelection(range.index + 1, Quill.sources.SILENT);
  }
}

function findPlaceholderInputContent(quill, componentsOutputVariables) {
  let value = quill.root.innerHTML;
  for (let i = 0; i < componentsOutputVariables.length; i++) {
    let variable = componentsOutputVariables[i];
    value = value.replaceAll('<span class="placeholder" data-placeholder=" ' +
      variable.name + ' ">﻿<span contenteditable="false"> ' +
      variable.name + ' </span>﻿</span>', "%" + variable.identifier + "%");
  }
  value = value.replaceAll("<br>", "");
  value = value.replaceAll("<p>", "");
  value = value.replaceAll("</p>", "\n");
  value = value.split('\n').slice(0, -1).join('');
  return value;
}
