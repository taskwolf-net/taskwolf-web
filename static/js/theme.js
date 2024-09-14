window.addEventListener('load', function () {
  let url = window.location.href.replace("https://dulno.com/", "").replaceAll("/", "");
  if (url === "" || url === "product" || url === "solution" || url === "pricing" ||
    url.includes("login") || url.includes("register") || url.includes("password") ||
    url.includes("offer") || url === "payment" || url === "paymentcomplete" ||
    url === "whitelist" || url === "imprint" || url === "privacy-policy"
  ) {
    return;
  }
  if (Cookie.find("dulno-theme") == null) {
    Cookie.create("dulno-theme", "dark", 60 * 60 * 24 * 365, ".dulno.com");
  }
  let theme = Cookie.find("dulno-theme");
  if (theme === "dark") {
    document.body.classList.add("dark");
  } else {
    document.body.classList.remove("dark");
    document.body.classList.add("light");
  }
});