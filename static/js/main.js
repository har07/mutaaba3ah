//date to yyyymmdd format string
//ref. http://stackoverflow.com/a/3067896/2998271
Date.prototype.toDateString = function() {
   var yyyy = this.getFullYear().toString();
   var mm = (this.getMonth()+1).toString(); // getMonth() is zero-based
   var dd  = this.getDate().toString();
   return yyyy + (mm[1]?mm:"0"+mm[0]) + (dd[1]?dd:"0"+dd[0]); // padding
  };

function getDateStringFromCalendar(cal){
    var result = cal.datepicker('getDate');
    if(result === null){
        return '';
    }
    return cal.datepicker('getDate').toDateString();
}

function updateReportData(){
    var datefrom = getDateStringFromCalendar($('#date_from'));
    var dateto = getDateStringFromCalendar($('#date_to'));
    var updateContent = function(data){
        $('#report_content').replaceWith(data);
    };
    var ajaxParams = {
        type: 'GET',
        url: '/mutaaba3ah/report/get_report_content/' + datefrom + '/' + dateto,
        dataType: 'html',
        success: updateContent
    };
     $.ajax(ajaxParams);
}

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

  //initiate jquery-ui tooltip
  $('[data-toggle="tooltip"]').tooltip({
    position: {
        my: "left bottom-10", // the "anchor point" in the tooltip element
        at: "left top", // the position of that anchor point relative to selected element
    }
  });

  //filter button
  $("input.btn-filter")
        .button()
        .click(function( event ) {
            event.preventDefault();
            updateReportData();
        });

//  $('.tilawah-spinner > input').spinner();

});