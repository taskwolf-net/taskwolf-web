window.addEventListener('load', function () {
  let request = new HttpRequest("/maintenance/scheduled/", "GET", []);
  request.send(function (status, responseText) {
    let maintenance = JSON.parse(responseText);
    if (!maintenance.found) {
      return;
    }
    displayMaintenanceBanner(maintenance);
  });
});

function displayMaintenanceBanner(maintenance) {
  let acknowledgedMaintenance = Cookie.find("maintenance");
  if (acknowledgedMaintenance === maintenance.id) {
    return;
  }
  let maintenanceBanner = document.createElement("div");
  maintenanceBanner.classList.add("maintenance-banner");
  maintenanceBanner.appendChild(document.createElement("div"));
  let maintenanceInformation = document.createElement("b");
  maintenanceInformation.classList.add("me-3");
  maintenanceInformation.innerHTML = buildMaintenanceInformation(maintenance);
  maintenanceBanner.appendChild(maintenanceInformation);
  let closeButton = document.createElement("a");
  closeButton.role = "button";
  closeButton.onclick = function (event) {
    acknowledgeMaintenance(maintenance);
  }
  let closeButtonIcon = document.createElement("h2");
  closeButtonIcon.classList.add("fa-solid", "fa-circle-xmark", "mb-0", "bg-dark",
    "rounded-circle");
  closeButton.appendChild(closeButtonIcon);
  maintenanceBanner.appendChild(closeButton);
  document.getElementsByTagName("body")[0].prepend(maintenanceBanner);
  let header = document.getElementById("navbar");
  if (header) {
    header.classList.add("maintenance-header");
    document.getElementById("header-space").classList.add("maintenance-header-space");
  }
}

function acknowledgeMaintenance(maintenance) {
  Cookie.create("maintenance", maintenance.id, 60 * 60 * 24 * 30);
  window.location.reload();
}

function buildMaintenanceInformation(maintenance) {
  let time = new Date(maintenance.startTime).toLocaleString();
  let duration = maintenance.duration / (1000 * 60);
  let format = generateMaintenanceInformationFormat();
  return format.replace("{0}", time).replace("{1}", duration);
}

function generateMaintenanceInformationFormat() {
  let language = "en";
  let homeLanguage = Cookie.find("dulno-home-language");
  let productLanguage = Cookie.find("dulno-language");
  if (homeLanguage != null) {
    language = homeLanguage.toLowerCase();
  } else if (productLanguage != null) {
    language = productLanguage.toLowerCase();
  }
  let text = "";
  if (language === "en") {
    text = "+++ Maintenance work on {0} - Estimated duration: {1} minutes - All services will be temporarily unavailable +++"
  } else if (language === "de") {
    text = "+++ Wartungsarbeiten am {0} - Geschätzte Dauer: {1} Minuten - Alle Dienste werden vorübergehend nicht verfügbar sein +++";
  }
  return text;
}

