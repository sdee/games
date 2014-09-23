$("#grid-basic").bootgrid();
$.fn.editable.defaults.mode = 'inline';
$(document).ready(function() {

    $(".editloc").editable(
      {
    type: 'text',
    pk: 1,
    url: '/post',
    title: 'Enter username'
}
    );
});
