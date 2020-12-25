$("#submit").click(function (e) {
  e.preventDefault();
  if ($("#bem-choice").val() != "") {
    let bemName = $(`#bem${$("#bem-choice").val()}`).data('name')
    let html = `
      <p>
      Setelah submit Anda tidak dapat memilih lagi. Apakah Anda yakin dengan pilihan Anda?
      </p>
      <ul>
        <li>Pilihan Ketua BEM: ${bemName}</li>
      </ul>
    `;
    $(".modal-body").html(html);
    $("#submit-form").removeClass("d-none");
  } else {
    let error = "Calon Ketua BEM.";
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
