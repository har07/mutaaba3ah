$(document).ready(function() {

  // listen to click events on search nav element
  $("#search-submit").on("click", function(e) {
    if (!$("#search-keywords").val()) {
      e.preventDefault();
      $("#search-keywords").toggleClass("hidden");
    }
  });


  //initiate jquery-ui datepicker
  $('.datepicker').datepicker({
        dateFormat: 'yy-mm-dd'
  });

  $('.tilawah-spinner > input').spinner();

});