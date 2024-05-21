var Cookie = {
  findAll: function () {
    var pairs = document.cookie.split(";");
    var cookies = {};
    for (var i = 0; i < pairs.length; i++){
      var pair = pairs[i].split("=");
      cookies[(pair[0]+'').trim()] = unescape(pair.slice(1).join("="));
    }
    return cookies;
  },

  find: function (name) {
    var cookie = null,
      list = this.findAll();
    var keys = Object.keys(list);
    for (var i = 0; i < keys.length; i++) {
      var key = keys[i];
      if (key === name) {
        cookie = list[key];
      }
    }
    return cookie;
  },

  create: function (name, value, time) {
    this.create(name, value, time, "." + location.host);
  },

  create: function (name, value, time, domain) {
    var today = new Date(),
      offset = (typeof time == "undefined") ? (1000 * 60 * 60 * 24) : (time * 1000),
      expires_at = new Date(today.getTime() + offset);
    var content = {
      name: escape(value),
      expires: expires_at.toGMTString(),
      path: "/",
      domain: domain,
      secure: true,
    };
    var cookie = Object.keys(content).map(function(key) {
      return [(key === "name") ? name : key, content[key]].join("=");
    }).join(";");
    document.cookie = cookie;
    return this;
  },

  destroy: function (name) {
    this.create(name, "", -1);
  },

  destroy: function (name, domain) {
    this.create(name, "", -1, domain);
  }
};