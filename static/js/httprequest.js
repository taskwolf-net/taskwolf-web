class HttpRequest {
  constructor(url, method, headers, data) {
    this.url = url;
    this.method = method;
    this.headers = headers;
    this.data = data;
  }

  send(callback) {
    let self = this;
    let headers = [...self.headers];
    headers.push({key: "Content-Type", value: "application/json"});
    let token = Cookie.find("token");
    if (token !== null) {
      headers.push({key: "Authorization", value: "Bearer " + token});
    }
    let homeToken = sessionStorage.getItem("home-token");
    if (homeToken !== null) {
      headers.push({key: "Home-Authorization", value: "Bearer " + homeToken});
    }
    let whitelistKey = Cookie.find("taskwolf-whitelist-key");
    if (whitelistKey !== null) {
      headers.push({key: "WHITELIST-KEY", value: whitelistKey});
    }
    const xhr = new XMLHttpRequest();
    xhr.open(self.method, self.url);
    for (const entry of headers) {
      xhr.setRequestHeader(entry.key, entry.value);
    }
    xhr.onload = function (e) {
      if (this.status === 417) {
        self.refresh(callback);
        return;
      }
      callback(this.status, xhr.responseText);
    };
    xhr.onerror = function (e) {
      callback(-1, "");
    };
    xhr.send(JSON.stringify(self.data));
  }

  refresh(callback) {
    let self = this;
    let refreshToken = Cookie.find("refresh-token");
    if (refreshToken == null) {
      return;
    }
    let request = new HttpRequest("https://api.taskwolf.net/v1/verification/refresh/", "POST",
      [], {refreshToken: refreshToken});
    request.send(function (status, responseText) {
      let response = JSON.parse(responseText);
      if (response.success === "true") {
        Cookie.create("token", response.productApiKey, 60 * 60 * 24 * 30, ".taskwolf.net");
        Cookie.create("refresh-token", response.refreshToken, 60 * 60 * 24 * 30, ".taskwolf.net");
        self.send(callback);
      }
    });
  }
}