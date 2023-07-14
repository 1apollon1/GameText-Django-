var ajax = new XMLHttpRequest();

ajax.onreadystatechange = function(){
    if (this.readyState == 4 && this.status == 200){
    console.log(Number(document.getElementById('rate').innerHTML), typeof this.responseText)
    document.getElementById('rate').innerHTML = Number(document.getElementById('rate').innerHTML) + this.responseText['rate']
    }
}

function react(pk, value){
    ajax.open('GET', rate(pk, value));
    ajax.send()
    document.getElementById('button_field').innerHTML = ''

    }

