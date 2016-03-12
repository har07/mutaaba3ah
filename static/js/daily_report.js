$(document).ready(function() {
    setChartGlobalSettings();
    updateDailyReportData();
});

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

function updateDailyReportData(){

    var ajaxParams = {
        type: 'GET',
        url: '/daily/daily_report/data',
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

function displayTilawah(data){
    //prepare chart data
    var labels = $.map(data, function(e){ return e.label; })
    var tilawah_data = $.map(data, function(e){ return e.tilawah; })
    var lineChartData = {
        labels : labels,
        datasets : [
            {
                label: "Jumlah halaman tilawah per hari",
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
        options: getChartOptions(40)
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
                label: "Jumlah raka'at dhuha per hari",
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
        options: getChartOptions(6)
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
                label: "Jumlah raka'at qiyamul lail per hari",
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
        options: getChartOptions(5)
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
                label: "Jumlah hari shaum per hari",
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
        options: getChartOptions(1)
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
                label: "Jumlah raport bersih per hari",
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
        options: getChartOptions(1)
    });
}
