$('#application_button').click(function(){
        console.log('dsadsadsa')
        $.ajax(
            {
               type: "GET",
               url: 'applicate/'+this.value,
               success: function(ans){
                   document.getElementById('application_div').innerHTML = '<b style="color: green">You applicated for join recently</b>'
                }
            }
        )
    }

)
