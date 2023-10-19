document.addEventListener("DOMContentLoaded", function () {
    const chatSocket = new WebSocket(
        "ws://" + window.location.host + "/ws/chat/"
    );

    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        const messageList = document.getElementById("message-list");
        const message = document.createElement("li");
        message.innerText = `${data.message}`;
        messageList.appendChild(message);
    };

    chatSocket.onclose = function (e) {
        console.error("Chat socket closed unexpectedly");
    };

    const messageForm = document.getElementById("message-form");
    messageForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const messageInput = document.getElementById("message-input");
        const message = messageInput.value;
        chatSocket.send(JSON.stringify({ message }));
        messageInput.value = "";
    });
});
