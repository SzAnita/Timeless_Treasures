function add_fav(name) {
    $.ajax({
            type: 'GET',
            url: 'add_fav/'+name,
            success: function (data) {
                if (JSON.parse(data) == "no") {
                    alert("You have to be logged in to add antiques to favorites.")
                } else{
                }
            }

    });
}