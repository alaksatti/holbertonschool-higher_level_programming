// fetches from URL and displays the value of hello from that fetch in the HTML’s tag DIV#hello.
$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  type: 'GET',
  dataType: 'json',
  success: function (response) {
    const salut = response.hello;

    $('DIV#hello').text(salut);
  }
});
