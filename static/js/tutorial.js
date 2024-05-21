let request = new HttpRequest("https://api.taskwolf.net/v1/tutorial/", "GET", []);
request.send(function (status, responseText) {
  var tutorial = JSON.parse(responseText);
  if (!tutorial.active) {
    return;
  }
  console.log(window.location.href + ":" + tutorial.page);
  if (!window.location.href.includes(tutorial.page)) {
    return;
  }
  displayTutorial(tutorial);
});

function displayTutorial(tutorial) {
  if (!window.location.href.includes(tutorial.page)) {
    window.location.href = tutorial.page;
    return;
  }
  Swal.fire({
    title: tutorial.title,
    text: tutorial.description,
    position: "top-end",
    showCancelButton: true,
    cancelButtonColor: "#dc3545",
    customClass: {
      container: "tutorial-container",
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
  document.querySelector(tutorial.element).classList.add("tutorial-highlight");
}

function cancelTutorial() {
  let request = new HttpRequest("https://api.taskwolf.net/v1/tutorial/cancel/", "POST", []);
  request.send(function (status, responseText) {
    var tutorial = JSON.parse(responseText);
    if (!tutorial.active) {
      return;
    }
    displayTutorial(tutorial);
  });
}

function continueTutorial() {
  let request = new HttpRequest("https://api.taskwolf.net/v1/tutorial/next/", "POST", []);
  request.send(function (status, responseText) {
    var tutorial = JSON.parse(responseText);
    if (!tutorial.active) {
      return;
    }
    displayTutorial(tutorial);
  });
}