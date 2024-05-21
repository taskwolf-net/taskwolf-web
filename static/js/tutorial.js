var highlightedElement = "";

let request = new HttpRequest("https://api.taskwolf.net/v1/tutorial/", "GET", []);
request.send(function (status, responseText) {
  var tutorial = JSON.parse(responseText);
  if (!tutorial.active) {
    return;
  }
  if (!window.location.href.includes(tutorial.page)) {
    return;
  }
  displayTutorial(tutorial, true);
});

function displayTutorial(tutorial, showCancel) {
  if (!window.location.href.includes(tutorial.page)) {
    window.location.href = tutorial.page;
    return;
  }
  if (tutorial.shiftContentDown) {
    document.getElementsByClassName("sidebar-influenced")[0].style.marginTop =
      "150px";
  }
  Swal.fire({
    title: tutorial.title,
    text: tutorial.description,
    position: tutorial.position,
    showCancelButton: showCancel,
    cancelButtonColor: "#dc3545",
    customClass: {
      container: "tutorial-container",
      popup: "tutorial-popup",
      actions: "tutorial-actions",
      confirmButton: "tutorial-continue",
      cancelButton: "tutorial-cancel",
    },
    confirmButtonText: tutorial.continue,
    cancelButtonText: tutorial.cancel
  }).then((result) => {
    if (result.dismiss === Swal.DismissReason.cancel) {
      cancelTutorial();
      return;
    }
    if (result.isConfirmed) {
      continueTutorial();
      return;
    }
  });
  if (highlightedElement !== "") {
    document.querySelector(highlightedElement).classList.remove("tutorial-highlight");
  }
  if (tutorial.element !== "") {
    document.querySelector(tutorial.element).classList.add("tutorial-highlight");
  }
  highlightedElement = tutorial.element;
}

function cancelTutorial() {
  let request = new HttpRequest("https://api.taskwolf.net/v1/tutorial/cancel/", "POST", []);
  request.send(function (status, responseText) {
    var tutorial = JSON.parse(responseText);
    if (!tutorial.active) {
      return;
    }
    displayTutorial(tutorial, false);
  });
}

function continueTutorial() {
  let request = new HttpRequest("https://api.taskwolf.net/v1/tutorial/next/", "POST", []);
  request.send(function (status, responseText) {
    var tutorial = JSON.parse(responseText);
    if (!tutorial.active) {
      return;
    }
    displayTutorial(tutorial, false);
  });
}