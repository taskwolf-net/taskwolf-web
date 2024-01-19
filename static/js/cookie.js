var Cookie = {
  findAll: function () {
    var pairs = document.cookie.split(";");
    var cookies = {};
    for (var i = 0; i < pairs.length; i++){
      var pair = pairs[i].split("=");
      cookies[(pair[0]+'').trim()] = unescape(pair.slice(1).join('='));
    }
    return cookies;
  },

  find: function (name) {
    var cookie = null,
      list = this.findAll();
    _.each(list, function (value, key) {
      if (key === name) cookie = value;
    });
    return cookie;
  },

  create: function (name, value, time) {
    var today = new Date(),
      offset = (typeof time == 'undefined') ? (1000 * 60 * 60 * 24) : (time * 1000),
      expires_at = new Date(today.getTime() + offset);

    var cookie = _.map({
      name: escape(value),
      expires: expires_at.toGMTString(),
      path: '/',
      domain: '.' + location.host,
      secure: true,
    }, function (value, key) {
      return [(key == 'name') ? name : key, value].join('=');
    }).join(';');

    document.cookie = cookie;
    return this;
  },

  destroy: function (name) {
    this.create(name, "", -1);
  }
};