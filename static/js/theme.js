window.addEventListener('load', function () {
  let url = window.location.href.replace("https://dulno.com/", "").replaceAll("/", "");
  if (url === "" || url === "product" || url === "solution" || url === "pricing" ||
    url.includes("login") || url.includes("register") || url.includes("password") ||
    url.includes("offer") || url.includes("download") || url === "payment" ||
    url === "paymentcomplete" || url === "whitelist" || url === "imprint" ||
    url === "privacy-policy" || url === "terms-of-service"
  ) {
    return;
  }
  if (Cookie.find("dulno-theme") == null) {
    Cookie.create("dulno-theme", "dark", 60 * 60 * 24 * 365, ".dulno.com");
  }
  let theme = Cookie.find("dulno-theme");
  var logoSource;
  if (theme === "dark") {
    document.body.classList.add("dark");
    logoSource = "logo-light.webp";
  } else {
    document.body.classList.remove("dark");
    document.body.classList.add("light");
    logoSource = "logo-dark.webp";
  }
  var logoElements = document.getElementsByClassName("dulno-logo");
  for (var i = 0; i < logoElements.length; i++) {
    logoElements[i].src = "https://dulno.com/static/img/" + logoSource;
  }
});