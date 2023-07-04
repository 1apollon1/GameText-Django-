 var chatlog = document.getElementById('chat-log');
 var actionlog = document.getElementById('action-log');
 const roomName = JSON.parse(document.getElementById('room-name').textContent);

        const chatSocket = new WebSocket(
            'ws://'
            + window.location.host
            + '/ws/chat/'
            + roomName
            + '/'
        );

        chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            if (data.message[0] != '!'){
                chatlog.innerHTML += data.message+'\n';
                chatlog.scrollTop = chatlog.scrollHeight;
            }
            else{
                actionlog.innerHTML += data.message.slice(1)+'\n';
                actionlog.scrollTop = chatlog.scrollHeight;
            }

        };

        chatSocket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };

        document.querySelector('#chat-message-input').focus();
        document.querySelector('#chat-message-input').onkeyup = function(e) {
            if (e.keyCode === 13) {  // enter, return
                document.querySelector('#chat-message-submit').click();
            }
        };

        document.querySelector('#chat-message-submit').onclick = function(e) {
            document.getElementById('chat-message-submit').disabled = true
            const messageInputDom = document.querySelector('#chat-message-input');
            const message = messageInputDom.value;
            chatSocket.send(JSON.stringify({
                'message': message
            }));
            messageInputDom.value = '';
        };
function InpReaction(){
    inpval = document.getElementById('chat-message-input').value
    if (inpval != ''){
        document.getElementById('chat-message-submit').disabled = false
    }
    else {
        document.getElementById('chat-message-submit').disabled = true
    }
}