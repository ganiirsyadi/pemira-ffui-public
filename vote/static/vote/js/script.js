function change(e) {
  e.preventDefault();
  // Change Title
  $("#title-bem").toggleClass("d-none");
  $("#title-bpm").toggleClass("d-none");
  // Change calons
  $("#calon-bem").toggleClass("d-flex");
  $("#calon-bem").toggleClass("d-none");
  $("#calon-bpm").toggleClass("d-flex");
  $("#calon-bpm").toggleClass("d-none");
  // Change button
  $("#bottom-btn").toggleClass("justify-content-between");
  $("#bottom-btn").toggleClass("justify-content-end");
  $("#next").toggleClass("d-none");
  $("#prev").toggleClass("d-none");
  $("#submit").toggleClass("d-none");
}
$("#next").click(function (e) {
  change(e);
});
$("#prev").click(function (e) {
  change(e);
});
$("#submit").click(function (e) {
  e.preventDefault();
  if ($("#bem-choice").val() != "" && $("#bpm-choice").val() != "") {
    let bemName = $(`#bem${$("#bem-choice").val()}`).data('name')
    let bpmName = $(`#bpm${$("#bpm-choice").val()}`).data('name')
    let html = `
      <p>
      Setelah submit Anda tidak dapat memilih lagi. Apakah Anda yakin dengan pilihan Anda?
      </p>
      <ul>
        <li>Pilihan Ketua BEM: ${bemName}</li>
        <li>Pilihan AI BPM: ${bpmName}</li>
      </ul>
    `;
    $(".modal-body").html(html);
    $("#submit-form").removeClass("d-none");
  } else {
    let error = "";
    if ($("#bem-choice").val() == "" && $("#bpm-choice").val() == "") {
      error = "Calon Ketua BEM maupun Calon Anggota Independen BPM.";
    } else if ($("#bem-choice").val() == "") {
      error = "Calon Ketua BEM.";
    } else {
      error = "Calon Anggota Independen BPM.";
    }
    let html = `
    <p>
      Anda belum memberikan pilihan pada ${error}
    </p>
  `;
    $(".modal-body").html(html);
    $("#submit-form").addClass("d-none");
  }
});
$(".pilih-bem").click(function (e) {
  e.preventDefault();
  $(".batal-bem").addClass("d-none");
  $(".pilih-bem").removeClass("d-none");
  $(".bem-card").css("background-color", "#FFE3C1");
  const el = $(this);
  el.toggleClass("d-none");
  el.next().toggleClass("d-none");
  el.parent().parent().css("background-color", "#E6BB89");
  $("#bem-choice").val(el.data("value"));
});
$(".batal-bem").click(function (e) {
  e.preventDefault();
  $(".batal-bem").addClass("d-none");
  $(".pilih-bem").removeClass("d-none");
  $(".bem-card").css("background-color", "#FFE3C1");
  $("#bem-choice").val("");
});
$(".pilih-bpm").click(function (e) {
  e.preventDefault();
  $(".batal-bpm").addClass("d-none");
  $(".pilih-bpm").removeClass("d-none");
  $(".bpm-card").css("background-color", "#FFE3C1");
  const el = $(this);
  el.toggleClass("d-none");
  el.next().toggleClass("d-none");
  el.parent().parent().css("background-color", "#E6BB89");
  $("#bpm-choice").val(el.data("value"));
});
$(".batal-bpm").click(function (e) {
  e.preventDefault();
  $(".batal-bpm").addClass("d-none");
  $(".pilih-bpm").removeClass("d-none");
  $(".bpm-card").css("background-color", "#FFE3C1");
  $("#bpm-choice").val("");
});
