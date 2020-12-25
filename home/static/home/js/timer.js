const current_date = new Date()
let countDownDate
// Countdown Vote
if (current_date < new Date(2020,11,4,7,30,0)) {
  countDownDate = new Date(2020, 11, 4, 7, 30, 0).getTime();
  $('#timer-date').html('4 Desember 2020 Pukul 07.30')
  $('#timer-info').html('Menuju Hari Pemilihan')
} else if (current_date < new Date(2020,11,9,18,0,0)) {
  countDownDate = new Date(2020, 11, 9, 18, 0, 0).getTime();
  $('#timer-date').html('9 Desember 2020 Pukul 18.00')
  $('#timer-info').html('Menuju Penutupan Pemungutan Suara')
} else if (current_date < new Date(2020,11,9,20,30,0)) {
  countDownDate = new Date(2020, 11, 9, 20, 30, 0).getTime();
  $('#timer-date').html('9 Desember 2020 Pukul 20.30')
  $('#timer-info').html('Menuju Pengumuman Hasil Pemungutan Suara')
} else if (current_date < new Date(2020,11,11,7,30,0)) {
  countDownDate = new Date(2020, 11, 11, 7, 30, 0).getTime();
  $('#timer-date').html('11 Desember 2020 Pukul 07.30')
  $('#timer-info').html('Menuju Pemilihan BEM Putaran Kedua')
} else if (current_date < new Date(2020,11,15,18,0,0)) {
  countDownDate = new Date(2020, 11, 15, 18, 0, 0).getTime();
  $('#timer-date').html('15 Desember 2020 Pukul 18.00')
  $('#timer-info').html('Menuju Penutupan Pemungutan Suara')
} else if (current_date < new Date(2020,11,15,20,0,0)) {
  countDownDate = new Date(2020, 11, 15, 20, 0, 0).getTime();
  $('#timer-date').html('15 Desember 2020 Pukul 20.00')
  $('#timer-info').html('Menuju Pengumuman Hasil Pemungutan Suara')
} else {
  $('.timer').removeClass('d-flex')
  $('.timer').addClass('d-none')
}
// Update the count down every 1 second
var x = setInterval(function () {
  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor(
    (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
  );
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element with id="demo"
  document.getElementById("timer-days").innerHTML =
    days < 10 ? "0" + days : days;
  document.getElementById("timer-hours").innerHTML =
    hours < 10 ? "0" + hours : hours;
  document.getElementById("timer-minutes").innerHTML =
    minutes < 10 ? "0" + minutes : minutes;
  document.getElementById("timer-seconds").innerHTML =
    seconds < 10 ? "0" + seconds : seconds;

  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
  }
}, 1000);
