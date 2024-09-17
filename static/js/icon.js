const updateIcon = (event) => {
  var iconElements = document.getElementsByClassName("dulno-icon");
  for (var i = 0; i < iconElements.length; i++) {
    if (event.matches) {
      iconElements[i].href = "https://dulno.com/static/img/icon-light.webp";
    } else {
      iconElements[i].href = "https://dulno.com/static/img/icon-dark.webp";
    }
  }
};

const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
updateIcon(mediaQuery);
mediaQuery.addEventListener('change', updateIcon);