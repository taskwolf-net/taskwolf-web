window.addEventListener('load', function () {
  if (Cookie.find("taskwolf-theme") == null) {
    Cookie.create("taskwolf-theme", "dark", 60 * 60 * 24 * 365, ".taskwolf.net");
  }
  var theme = Cookie.find("taskwolf-theme");
  if (theme === "dark") {
    document.body.classList.add("dark");
  } else {
    document.body.classList.add("light");
  }
});