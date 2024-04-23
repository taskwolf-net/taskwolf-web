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
      callback(this.status, xhr.responseText);
    };
    xhr.onerror = function (e) {
      callback(-1, "");
    };
    xhr.send(JSON.stringify(this.data));
  }
}