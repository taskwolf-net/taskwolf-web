window.addEventListener('load', function () {
  let url = window.location.href.replace("https://taskwolf.net/", "").replaceAll("/", "");
  if (url === "" || url === "product" || url === "solution" || url === "pricing" ||
    url.includes("login") || url.includes("register") || url.includes("password") ||
    url.includes("offer") || url === "payment" || url === "paymentcomplete" ||
    url === "whitelist" || url === "imprint" || url === "privacy-policy"
  ) {
    return;
  }
  if (Cookie.find("taskwolf-theme") == null) {
    Cookie.create("taskwolf-theme", "dark", 60 * 60 * 24 * 365, ".taskwolf.net");
  }
  let theme = Cookie.find("taskwolf-theme");
  if (theme === "dark") {
    document.body.classList.add("dark");
  } else {
    document.body.classList.remove("dark");
    document.body.classList.add("light");
  }
});