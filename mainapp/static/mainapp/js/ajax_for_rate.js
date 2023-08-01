$('.reaction').click(function(){
    $.ajax(
        {
            type:"GET",
            url: '/rate/'+this.value+'/'+this.id,
            success: function( ans )
                {
                    document.getElementById(ans['pk']+'rate').innerHTML = ans['rate']
                    document.getElementById(ans['pk']+'button_field').innerHTML = ''
                }
         })
})

