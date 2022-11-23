const addTag = $('DIV#add_item');
const getClass = $('UL.my_list');

addTag.click(function () {
  const liTag = $('<li></li>').text('Item');
  getClass.append(liTag);
});
