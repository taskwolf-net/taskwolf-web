class HttpRequest {
  constructor(url, method, headers, data) {
    this.url = url;
    this.method = method;
    this.headers = headers;
    this.data = data;
  }

  send(callback) {
    this.headers.push({key: "Content-Type", value: "application/json"});
    var token = Cookie.find("token");
    if (token !== null) {
      this.headers.push({key: "Authorization", value: "Bearer " + token});
    }
    var homeToken = sessionStorage.getItem("home-token");
    if (homeToken !== null) {
      this.headers.push({key: "Home-Authorization", value: "Bearer " + homeToken});
    }
    var whitelistKey = Cookie.find("taskwolf-whitelist-key");
    if (whitelistKey !== null) {
      this.headers.push({key: "WHITELIST-KEY", value: whitelistKey});
    }
    const xhr = new XMLHttpRequest();
    xhr.open(this.method, this.url);
    for (const entry of this.headers) {
      xhr.setRequestHeader(entry.key, entry.value);
    }
    xhr.onload = function (e) {
      if (this.status === 417) {
        this.refresh(callback);
        return;
      }
      callback(this.status, xhr.responseText);
    };
    xhr.onerror = function (e) {
      callback(-1, "");
    };
    xhr.send(JSON.stringify(this.data));
  }


  refresh(callback) {
    var refreshToken = Cookie.find("refresh-token");
    if (refreshToken == null) {
      return;
    }
    let request = new HttpRequest("https://api.taskwolf.net/v1/verification/refresh/", "POST",
      [], {refreshToken: refreshToken});
    request.send(function (status, responseText) {
      var response = JSON.parse(responseText);
      if (response.success === "true") {
        Cookie.create("token", response.productApiKey, 60 * 60 * 24 * 30, ".taskwolf.net");
        Cookie.create("refresh-token", response.refreshToken, 60 * 60 * 24 * 30, ".taskwolf.net");
        this.send(callback);
      }
    });
  }
}