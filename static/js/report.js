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

function toggleGridButtons(isEnable){
    //toggle enable-disable buttons
    $(".btn-grid").prop("disabled", isEnable);

    //remove previously attached event handle
    //add new event handler relevant to currently selected row
    $('#edit').off("click");
    $('#edit:enabled').on("click", function(event){
        event.preventDefault();
        var url = $('.table.selectable > tbody > tr.success .edit-url').text();
        window.open(url);
    });
    $('#delete').off("click");
    $('#delete:enabled').on("click", function(event){
        event.preventDefault();
        var url = $('.table.selectable > tbody > tr.success .delete-url').text();
        window.open(url);
    });
}

$(document).ready(function() {
    $('.table.selectable > tbody > tr').click(function(e){
        //on row selected toggle row color
        //only one row can be selected at a time
        //toggle (enable/disable) Edit & Delete button
        //set url for Edit & Delete selected row
        $(this).toggleClass("success");
        $(this).siblings().removeClass("success");
        var isEnable = !$(this).hasClass("success");
        toggleGridButtons(isEnable);
    });

//    $(".mutaaba3ah-date").css("cursor","pointer")
//                         .tooltip()
//                         .click(function(e){
//         var url = $(".table.selectable > tbody > tr.success .view-url").text();
//         window.open(url);
//     });

    $("input.btn-filter")
        .button()
        .click(function( event ) {
            //on click, update HTML of report_content.html
            event.preventDefault();
            updateReportData();
        });
});