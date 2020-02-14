// print hello in input language
$(function () {
  $('#btn_translate').click(function () {
    const value = $('INPUT#language_code').val();
    $.ajax({
      url: 'https://fourtonfish.com/hellosalut/?lang=' + value,
      type: 'GET',
      dataType: 'json',
      success: function (response) {
        $('DIV#hello').append(`${response.hello}<br>`);
      }
    });
  });
});
