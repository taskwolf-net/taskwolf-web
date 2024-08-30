window.addEventListener('load', function () {
  let request = new HttpRequest("https://api.taskwolf.net/v1/maintenance/scheduled/", "GET", []);
  request.send(function (status, responseText) {
    var maintenance = JSON.parse(responseText);
    if (!maintenance.found) {
      return;
    }
    displayMaintenanceBanner(maintenance);
  });
});

function displayMaintenanceBanner(maintenance) {
  var acknowledgedMaintenance = Cookie.find("maintenance");
  if (acknowledgedMaintenance === maintenance.id) {
    return;
  }
  var maintenanceBanner = document.createElement("div");
  maintenanceBanner.classList.add("maintenance-banner");
  maintenanceBanner.appendChild(document.createElement("div"));
  var maintenanceInformation = document.createElement("b");
  maintenanceInformation.innerHTML = buildMaintenanceInformation(maintenance);
  maintenanceBanner.appendChild(maintenanceInformation);
  var closeButton = document.createElement("a");
  closeButton.role = "button";
  closeButton.onclick = function (event) {
    acknowledgeMaintenance(maintenance);
  }
  var closeButtonIcon = document.createElement("h2");
  closeButtonIcon.classList.add("fa-solid", "fa-circle-xmark", "mb-0", "bg-dark",
    "rounded-circle");
  closeButton.appendChild(closeButtonIcon);
  maintenanceBanner.appendChild(closeButton);
  document.getElementsByTagName("body")[0].prepend(maintenanceBanner);
  var header = document.getElementById("navbar");
  if (header) {
    header.classList.add("maintenance-header");
    document.getElementById("header-space").classList.add("maintenance-header-space");
  }
}

function acknowledgeMaintenance(maintenance) {
  Cookie.create("maintenance", maintenance.id, 60 * 60 * 24 * 30, ".taskwolf.net");
  window.location.reload();
}

function buildMaintenanceInformation(maintenance) {
  var time = new Date(maintenance.startTime).toLocaleString();
  var duration = maintenance.duration / (1000 * 60);
  var format = generateMaintenanceInformationFormat();
  return format.replace("{0}", time).replace("{1}", duration);
}

function generateMaintenanceInformationFormat() {
  var language = "en";
  var homeLanguage = Cookie.find("taskwolf-home-language");
  var productLanguage = Cookie.find("taskwolf-language");
  if (homeLanguage != null) {
    language = homeLanguage.toLowerCase();
  } else if (productLanguage != null) {
    language = productLanguage.toLowerCase();
  }
  var text = "";
  if (language === "en") {
    text = "+++ Maintenance work on {0} - Estimated duration: {1} minutes +++";
  } else if (language === "de") {
    text = "+++ Wartungsarbeiten am {0} - Geschätzte Dauer: {1} Minuten +++";
  }
  return text;
}

