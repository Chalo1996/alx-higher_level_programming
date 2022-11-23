const getDivHello = $('DIV#hello');
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$.getJSON(url, { hello: 'Hello' }, function (data) {
  const getHello = data;
  const addTag = $('<p></p>').text(getHello);
  getDivHello.append(addTag);
});
