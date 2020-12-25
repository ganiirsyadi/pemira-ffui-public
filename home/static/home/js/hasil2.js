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
      ["M. Najmi", "Shobari"],
      ["M. Hibban", "Arasy"],
    ],
    datasets: [
      {
        label: ["Perolehan Suara"],
        data: [dbem.bem2, dbem.bem3],
        backgroundColor: [
          "rgba(230,187,137,0.9)",
          "rgba(85,92,83,0.9)",
        ],
        hoverBackgroundColor: [
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
var chart = new Chart(cbem, myChartBem);

$('#dpt-bem').html(`Pemilih yang Menggunakan Hak Pilih: ${dbem.total} Pemilih`)
