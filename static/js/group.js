const group_id = JSON.parse(document.getElementById('json-username').textContent);
const loggedin_user = JSON.parse(document.getElementById('json-message-username').textContent);
const group_name = JSON.parse(document.getElementById('json-username-receiver').textContent);

const socket = new WebSocket('ws://' + window.location.host + '/ws/group_chat/' + group_id + '/');

socket.onopen = function(e){
    console.log("CONNECTION ESTABLISHED");
}

socket.onclose = function(e){
    console.log("CONNECTION LOST");
}

socket.onerror = function(e){
    console.log("ERROR OCCURED");
}

socket.onmessage = function(e){
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

    socket.send(JSON.stringify({
        'message':message,
        'username':loggedin_user,
        'receiver':group_name
    }));

    message_input.value = '';
}
