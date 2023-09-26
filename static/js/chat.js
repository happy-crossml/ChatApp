const id = JSON.parse(document.getElementById('json-username').textContent);
const message_username = JSON.parse(document.getElementById('json-message-username').textContent);
const receiver = JSON.parse(document.getElementById('json-username-receiver').textContent);

const personal_socket = new WebSocket('ws://' + window.location.host + '/ws/personal/' + id + '/');

personal_socket.onopen = function(e){
    console.log("CONNECTION ESTABLISHED");
}

personal_socket.onclose = function(e){
    console.log("CONNECTION LOST");
}

personal_socket.onerror = function(e){
    console.log("ERROR OCCURED");
}

personal_socket.onmessage = function(e){
    const data = JSON.parse(e.data);
    const messageContainer = document.querySelector('#chat-body');
    
    if (data.username == message_username) {
        messageContainer.insertAdjacentHTML('beforeend', `<tr><td><p class="bg-success p-2 mt-2 mr-5 shadow-sm text-white float-right rounded">${data.message}</p></td></tr>`);
    } else {
        messageContainer.insertAdjacentHTML('beforeend', `<tr><td><p class="bg-primary p-2 mt-2 mr-5 shadow-sm text-white float-left rounded">${data.message}</p></td></tr>`);
    }
}

document.querySelector('#chat-message-submit').onclick = function(e){
    const message_input = document.querySelector('#message_input');
    const message = message_input.value;

    personal_socket.send(JSON.stringify({
        'message':message,
        'username':message_username,
        'receiver':receiver
    }));

    message_input.value = '';
}
