var currentTarget;

function setupTargetSelection(callback) {
  fetchTargetsData(function(response) {
    var targets = response.targets;
    for (var i = 0; i < targets.length; i++) {
      addTarget(targets[i]);
    }
    currentTarget = targets.filter((target) =>
      target.id === response.currentTarget)[0];
    document.getElementById("target-dropdown-button").innerHTML +=
      currentTarget.name;
    callback();
  });
}

function fetchTargetsData(callback) {
  let request = new HttpRequest("https://api.taskwolf.net/v1/targets/all/", "GET",
    []);
  request.send(function (status, responseText) {
    callback(JSON.parse(responseText));
  });
}

function addTarget(target) {
  var targetElement = document.createElement("li");
  targetElement.classList.add("dropdown-item");
  var targetNameName = document.createElement("b");
  targetNameName.innerHTML = target.name;
  targetElement.appendChild(targetNameName);
  targetElement.onclick = function(event) {
    selectTarget(target);
  }
  document.getElementById("target-dropdown-list").appendChild(targetElement);
}

function selectTarget(target) {
  let request = new HttpRequest("https://api.taskwolf.net/v1/target/change/", "POST",
    [], {target: target.id});
  request.send(function (status, responseText) {
    window.location.reload();
  });
}