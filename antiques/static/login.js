function check_pwd() {
    let pwd = $('#id_pwd').val();
    let pwd2 = $('#id_pwd2').val();
    if (pwd != pwd2) {
        $('#pwd2').after("<p class='invalid'>You might have mistyped something.</p>")
    } else {
        $('#pwd2').after("<p class='invalid'>Everything is okay</p>")
    }
}