const ulGetTag = $('UL#list_movies');

const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.getJSON(url, function (data) {
  const getTitlesLen = data.results.length;

  for (let i = 0; i < getTitlesLen; i++) {
    const addTag = $('<li></li>').text(data.results[i].title);
    ulGetTag.append(addTag);
  }
});
