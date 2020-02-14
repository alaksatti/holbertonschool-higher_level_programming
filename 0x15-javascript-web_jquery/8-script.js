// fetches and lists all movies title by using this URL: https://swapi.co/api/films/?format=json
$.ajax({
  url: 'https://swapi.co/api/films/?format=json',
  type: 'GET',
  dataType: 'json',
  success: function (response) {
    const films = response.results;
    for (let i = 0; i < films.length; i++) {
      $('UL#list_movies').append('<li>' + films[i].title + '</li>');
    }
  }
});
