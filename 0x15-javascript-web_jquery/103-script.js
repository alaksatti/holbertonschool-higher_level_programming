// print hello in input language when click or enter
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
  $('INPUT#language_code').on('keypress', function (e) {
    if (e.which === 13) {
      const value = $('INPUT#language_code').val();
      $.ajax({
        url: 'https://fourtonfish.com/hellosalut/?lang=' + value,
        type: 'GET',
        dataType: 'json',
        success: function (response) {
          $('DIV#hello').append(`${response.hello}<br>`);
        }
      });
    }
  });
});
