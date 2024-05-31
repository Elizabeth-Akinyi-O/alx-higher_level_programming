const $ = window.$;
$(document).ready(function () {
  $('div#red_header').click(function () {
    $('div#red_header').css('color', '#FF0000');
  });
});
