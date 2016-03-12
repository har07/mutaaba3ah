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
    displayTilawah(data);
    displayDhuha(data);
    displayQl(data);
    displayShaum(data);
    displayRaport(data);
}

function dummyChartData(){
    var randomScalingFactor = function(){ return Math.round(Math.random()*100)};
    var lineChartData = {
        labels : ["January","14 - 20 February","21 - 27 February","28 February - 5 March","May","June","July"],
        datasets : [
            {
                label: "My First dataset",
//                fillColor : "rgba(220,220,220,0.2)",
                fill: false,
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
        var ctx = document.getElementById("tilawahChart").getContext("2d");
        window.myLine = new Chart(ctx, {
            type: 'line',
            data: lineChartData
        });
    }
}

function setChartGlobalSettings(){
    Chart.defaults.global.responsive = true;
    Chart.defaults.global.elements.line.tension = 0;
}

function getChartOptions(suggestedMax){
    return {
        tension: 0, //straight lines
        responsive: true,
        scales: {
            yAxes: [{
                display: true,
                ticks: {
                    suggestedMin: 0    // minimum will be 0, unless there is a lower value.
                    ,suggestedMax: suggestedMax
                }
            }]
        }
    };
}

$(document).ready(function() {
    setChartGlobalSettings();
    updateReportData();
//    dummyChartData();
});

function displayTilawah(data){
    //prepare chart data
    var labels = $.map(data, function(e){ return e.label; })
    var tilawah_data = $.map(data, function(e){ return e.tilawah; })
    var lineChartData = {
        labels : labels,
        datasets : [
            {
                label: "Jumlah halaman tilawah per pekan",
//                fillColor : "rgba(220,220,220,0.2)",
                fill: false,
                strokeColor : "rgba(220,220,220,1)",
                pointColor : "rgba(220,220,220,1)",
                pointStrokeColor : "#fff",
                pointHighlightFill : "#fff",
                pointHighlightStroke : "rgba(220,220,220,1)",
                data : tilawah_data
            }
        ]
    }

    //update chart with data
    var ctx = document.getElementById("tilawahChart").getContext("2d");
    window.myLine = new Chart(ctx, {
        type: 'line',
        data: lineChartData,
        options: getChartOptions(200)
    });
}

function displayDhuha(data){
    //prepare chart data
    var labels = $.map(data, function(e){ return e.label; })
    var dhuha = $.map(data, function(e){ return e.dhuha; })
    var lineChartData = {
        labels : labels,
        datasets : [
            {
                label: "Jumlah raka'at dhuha per pekan",
//                fillColor : "rgba(220,220,220,0.2)",
                fill: false,
                strokeColor : "rgba(220,220,220,1)",
                pointColor : "rgba(220,220,220,1)",
                pointStrokeColor : "#fff",
                pointHighlightFill : "#fff",
                pointHighlightStroke : "rgba(220,220,220,1)",
                data : dhuha
            }
        ]
    }

    //update chart with data
    var ctx = document.getElementById("dhuhaChart").getContext("2d");
    window.myLine = new Chart(ctx, {
        type: 'line',
        data: lineChartData,
        options: getChartOptions(28)
    });
}

function displayQl(data){
    //prepare chart data
    var labels = $.map(data, function(e){ return e.label; })
    var ql = $.map(data, function(e){ return e.ql; })
    var lineChartData = {
        labels : labels,
        datasets : [
            {
                label: "Jumlah raka'at qiyamul lail per pekan",
//                fillColor : "rgba(220,220,220,0.2)",
                fill: false,
                strokeColor : "rgba(220,220,220,1)",
                pointColor : "rgba(220,220,220,1)",
                pointStrokeColor : "#fff",
                pointHighlightFill : "#fff",
                pointHighlightStroke : "rgba(220,220,220,1)",
                data : ql
            }
        ]
    }

    //update chart with data
    var ctx = document.getElementById("qlChart").getContext("2d");
    window.myLine = new Chart(ctx, {
        type: 'line',
        data: lineChartData,
        options: getChartOptions(21)
    });
}

function displayShaum(data){
    //prepare chart data
    var labels = $.map(data, function(e){ return e.label; })
    var shaum = $.map(data, function(e){ return e.shaum; })
    var lineChartData = {
        labels : labels,
        datasets : [
            {
                label: "Jumlah hari shaum per pekan",
//                fillColor : "rgba(220,220,220,0.2)",
                fill: false,
                strokeColor : "rgba(220,220,220,1)",
                pointColor : "rgba(220,220,220,1)",
                pointStrokeColor : "#fff",
                pointHighlightFill : "#fff",
                pointHighlightStroke : "rgba(220,220,220,1)",
                data : shaum
            }
        ]
    }

    //update chart with data
    var ctx = document.getElementById("shaumChart").getContext("2d");
    window.myLine = new Chart(ctx, {
        type: 'line',
        data: lineChartData,
        options: getChartOptions(3)
    });
}

function displayRaport(data){
    //prepare chart data
    var labels = $.map(data, function(e){ return e.label; })
    var raport = $.map(data, function(e){ return e.raport; })
    var lineChartData = {
        labels : labels,
        datasets : [
            {
                label: "Jumlah raport bersih per pekan",
//                fillColor : "rgba(220,220,220,0.2)",
                fill: false,
                strokeColor : "rgba(220,220,220,1)",
                pointColor : "rgba(220,220,220,1)",
                pointStrokeColor : "#fff",
                pointHighlightFill : "#fff",
                pointHighlightStroke : "rgba(220,220,220,1)",
                data : raport
            }
        ]
    }

    //update chart with data
    var ctx = document.getElementById("raportChart").getContext("2d");
    window.myLine = new Chart(ctx, {
        type: 'line',
        data: lineChartData,
        options: getChartOptions(7)
    });
}
