Chart.helpers.merge(Chart.defaults.global.plugins.datalabels, {
  color: "#333333",
  font: {
    size: 13,
    weight: 'bold'
  },
  anchor: 'end',
  align: 'end',
  offset: 6
});
var cbem = $("#myChartBEM");
var dbem = cbem.data("result");
var myChartBem = {
  type: "horizontalBar",
  data: {
    labels: [
      ["Trixie Putri", "Padita"],
      ["M. Najmi", "Shobari"],
      ["M. Hibban", "Arasy"],
    ],
    datasets: [
      {
        label: ["Perolehan Suara"],
        data: [dbem.bem1, dbem.bem2, dbem.bem3],
        backgroundColor: [
          "rgba(138,71,66,0.9)",
          "rgba(230,187,137,0.9)",
          "rgba(85,92,83,0.9)",
        ],
        hoverBackgroundColor: [
          "rgba(138,71,66,1)",
          "rgba(230,187,137,1)",
          "rgba(85,92,83,1)",
        ],
        barPercentage: 0.8,
      },
    ],
  },
  options: {
    plugins: {
      datalabels: {
        formatter: function(value, context) {
          return ((value/dbem.total) * 100).toFixed(2) + '%'
        }
      }
    },
    legend: {
      display: false,
    },
    responsive: true,
    scales: {
      xAxes: [
        {
          ticks: {
            max: Math.floor(Math.ceil(dbem.max * (10/9)) / 10) * 10 + 10,
            min: 0,
            stepSize: 10,
          },
        },
      ],
    },
  },
};
var cbpm = $("#myChartBPM");
var dbpm = cbpm.data("result");
var myChartBpm = {
  type: "horizontalBar",
  data: {
    labels: [
      ["Krisastra", "Halim"],
      ["Syafura", "Az-Zahra"],
      ["Farhan", "Eviansyah"],
    ],
    datasets: [
      {
        label: ["Perolehan Suara"],
        data: [dbpm.bpm1, dbpm.bpm2, dbpm.bpm3],
        backgroundColor: [
          "rgba(138,71,66,0.9)",
          "rgba(230,187,137,0.9)",
          "rgba(85,92,83,0.9)",
        ],
        hoverBackgroundColor: [
          "rgba(138,71,66,1)",
          "rgba(230,187,137,1)",
          "rgba(85,92,83,1)",
        ],
        barPercentage: 0.8,
      },
    ],
  },
  options: {
    plugins: {
      datalabels: {
        formatter: function(value, context) {
          return ((value/dbpm.total) * 100).toFixed(2) + '%'
        }
      }
    },
    legend: {
      display: false,
    },
    responsive: true,
    scales: {
      xAxes: [
        {
          ticks: {
            max: Math.floor(Math.ceil(dbpm.max * (10/9)) / 10) * 10 + 10,
            min: 0,
            stepSize: 10,
          },
        },
      ],
    },
  },
};
var chart = new Chart(cbem, myChartBem);
$(".change-result").click(function () {
  $("#myChartBEM").toggleClass("d-none");
  $("#myChartBPM").toggleClass("d-none");
  $(".change-result").toggleClass("d-none");
  $(".hasil").toggleClass("d-none");
  $(".dpt").toggleClass("d-none");
  chart.destroy();
  if ($("#myChartBEM").hasClass("d-none")) {
    chart = new Chart(cbpm, myChartBpm);
  } else {
    chart = new Chart(cbem, myChartBem);
  }
});

$('#dpt-bem').html(`Pemilih yang Menggunakan Hak Pilih: ${dbem.total} Pemilih`)
$('#dpt-bpm').html(`Pemilih yang Menggunakan Hak Pilih: ${dbpm.total} Pemilih`)