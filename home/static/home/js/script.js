$(document).scroll(function () {
  var $nav = $(".fixed-top");
  $nav.toggleClass("scrolled", $(this).scrollTop() > $nav.height());
});

const now = new Date()

// Close Registration
const closeReg = new Date(2020,11,4,0,0,0)
if (now < closeReg) {
  $('#nav-register').removeClass('d-none')
}

// Reveal Result
const startHide = new Date(2020,11,11,7,30,0)
const finishHide = new Date(2020,11,15,20,0,0)
if (startHide < now && now < finishHide) {
  $('#nav-result').addClass('d-none')
}