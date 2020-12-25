$('#file').change(function(e) { 
  const file = e.currentTarget.files[0];
  if (file.size > 1024 * 1024 * 2) {
    alert("Ukuran file terlalu besar")
    $('#file').val(null)
  } else {
    $('.file-box').css('display', 'flex')
    $('.upload-box').css('display', 'none')
    $('#filename').html(file.name)
  }
})
