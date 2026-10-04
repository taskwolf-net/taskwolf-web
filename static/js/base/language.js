window.addEventListener('load', function () {
  if (Cookie.find("taskwolf-home-language") != null) {
    return;
  }
  var language = navigator.language || navigator.userLanguage;
  if (language !== "en" && language !== "de") {
    language = "en";
  }
  Cookie.create("taskwolf-home-language", language, 60 * 60 * 24 * 365);
});