function updateReportData(){

    var ajaxParams = {
        type: 'GET',
        url: '/daily/weekly_report/data',
        dataType: 'json',
        success: updateChart,
        error: function(msg){
            alert(msg);
        }
    };
     $.ajax(ajaxParams);
}

function updateChart(data){
    //prepare chart data
    var labels = $.map(data, function(e){ return e.label; })
    var tilawah_data = $.map(data, function(e){ return e.tilawah; })
    var lineChartData = {
        labels : labels,
        datasets : [
            {
                label: "Jumlah halaman tilawah per pekan",
                fillColor : "rgba(220,220,220,0.2)",
                strokeColor : "rgba(220,220,220,1)",
                pointColor : "rgba(220,220,220,1)",
                pointStrokeColor : "#fff",
                pointHighlightFill : "#fff",
                pointHighlightStroke : "rgba(220,220,220,1)",
                data : tilawah_data
            }
        ]
    }

    //update chart with prepared data
    var ctx = document.getElementById("canvas").getContext("2d");
    window.myLine = new Chart(ctx).Line(lineChartData, {
        bezierCurve : false,
        responsive: true
    });
}

function applyChartSettings(){
    var ctx = document.getElementById("canvas").getContext("2d");
    window.myLine = new Chart(ctx).Line(lineChartData, {
        bezierCurve : false,
        responsive: true
    });
}

function dummyChartData(){
    var randomScalingFactor = function(){ return Math.round(Math.random()*100)};
    var lineChartData = {
        labels : ["January","14 - 20 February","21 - 27 February","28 February - 5 March","May","June","July"],
        datasets : [
            {
                label: "My First dataset",
                fillColor : "rgba(220,220,220,0.2)",
                strokeColor : "rgba(220,220,220,1)",
                pointColor : "rgba(220,220,220,1)",
                pointStrokeColor : "#fff",
                pointHighlightFill : "#fff",
                pointHighlightStroke : "rgba(220,220,220,1)",
                data : [620,219,625,594,633,824,983,647,613,637,611,632]
            },
            {
                label: "My Second dataset",
                fillColor : "rgba(151,187,205,0.2)",
                strokeColor : "rgba(151,187,205,1)",
                pointColor : "rgba(151,187,205,1)",
                pointStrokeColor : "#fff",
                pointHighlightFill : "#fff",
                pointHighlightStroke : "rgba(151,187,205,1)",
                data : [98,113,137,161,466,663,1178,627,488,622,604,631]
            }
        ]

    }

    window.onload = function(){
        var ctx = document.getElementById("canvas").getContext("2d");
        window.myLine = new Chart(ctx).Line(lineChartData, {
            bezierCurve : false,
            responsive: true
        });
    }
}

$(document).ready(function() {
//    updateReportData();
    dummyChartData();
});
