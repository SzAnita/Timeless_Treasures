  function display_form (name) {
        $.ajax({
            type: 'GET',
            url: 'get_coll',
            data: {
                'antique':name
            },
            success: function (result) {
                let data = JSON.parse(result);
                if(data == 'login') {
                    $(location).prop('href', 'login')
                }
                let name = data[0];
                let form = $("<form></form>");
                form.attr({
                    'action':'add_collection/'+name,
                    'method':'GET',
                    'id':name+'_form',
                    'class':'add_coll'
                });
                for (let i=0; i<data[1].length; i++) {
                    $(form).append("<label><input type='radio' name='coll' id='"+data[1][i]+"' value='"+data[1][i]+"'>"+data[1][i]+"<br></label>")
                }
                let link_new = $("<a></a>").html("Add new collection<br>");
                link_new.attr({
                    'class':'new_coll',
                    'onclick': "new_coll('"+name+"')"
                });
                $(form).append(link_new);
                let input = $("<input type='submit' value='Submit'>");
                $(form).append(input);
                $("[id ='"+name+"']").empty().append(form);
            }
        });
}
function new_coll(name) {
    let c = prompt("Create a new collection");
    if (c != null) {
        let label = $("<label></label>");
        let input = $("<input>").html(c + "<br>");
        input.attr({
            'type': 'radio',
            'name': 'coll',
            'id': c,
            'value': c
        });
        $(label).append(input);
        $("[id ='" + name + "_form'] label").before(label);
        $.ajax({
            url: 'update_coll',
            type: 'GET',
            data: {
                'name': c
            }
        });
    }
}



