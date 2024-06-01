#!/usr/bin/node
const $ = window.$;
$(document).ready(function () {
  $('DIV#update_header').click(function () {
    $('HEADER').text('New Header!!!');
  });
});
