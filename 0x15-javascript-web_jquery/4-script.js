const getHeader = $('header');

const getDivToggleClass = $('DIV#toggle_header');

getDivToggleClass.click(function () {
  getHeader.toggleClass('green');
  getHeader.toggleClass('red');
});
