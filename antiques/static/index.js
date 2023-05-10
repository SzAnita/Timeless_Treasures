function add_fav(name) {
     $.ajax({
         type: 'GET',
         url: 'add_fav/' + name
     });
}

