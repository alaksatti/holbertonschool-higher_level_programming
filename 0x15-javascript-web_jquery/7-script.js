// fetches and replaces the name of the URL
$.ajax({
  url: 'https://swapi.co/api/people/5/?format=json',
  type: 'GET',
  dataType: 'json',
  success: function (response) {
    $('div#character').text(response.name);
  }
});
