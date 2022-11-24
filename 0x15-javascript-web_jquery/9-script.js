const getDivHello = $('DIV#hello');
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$(function () {
  $.getJSON(url, function (data) {
    const getHello = JSON.stringify(data).hello;
    const addTag = $('<p></p>').text(getHello);
    getDivHello.append(addTag);
  });
});
