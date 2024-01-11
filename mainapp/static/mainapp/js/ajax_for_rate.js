function getElementInsideContainer(containerID, childID) {
   var elm = document.getElementById(containerID).querySelector('#' + childID);
   return elm ? elm : {};
}


$('.reaction').click(function(){
    $.ajax(
        {
            type:"GET",
            headers: {
                "Accept": "application/json; odata=verbose"
            },
            data: JSON.stringify(23),
            processData: false,
            url: '/rate/'+this.value+'/'+this.id,
            success: function( ans )
                {
                    document.getElementById(ans['pk']+'rate').innerHTML = ans['rate']
                    var buttonup = getElementInsideContainer(ans['pk']+'button_field', 'up')
                    var buttondown = getElementInsideContainer(ans['pk']+'button_field', 'down')
                    if (ans['blue_button'] == 'r'){
                        buttonup.style.background = 'blue'
                        buttondown.style.background = null
                    }
                    else if (ans['blue_button'] == 'l'){
                        buttondown.style.background = 'blue'
                        buttonup.style.background = null
                    }

                    else{
                        console.log('all in null')
                        buttondown.style.background =  null
                        buttonup.style.background = null
                    }

                }
         })
})

