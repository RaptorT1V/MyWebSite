function showPopupMessage(message, messageType = 'good') {
    const popup = document.getElementById('popup-message');
    popup.textContent = message;

    if (messageType === 'bad') {
        popup.classList.add('popup-message-bad');
    } else {
        popup.classList.add('popup-message-good');
    }

    if (message.trim() !== "") {
        popup.classList.add('show');
        setTimeout(() => {
            popup.classList.remove('show');
        }, 2750);
    }
}

window.addEventListener('DOMContentLoaded', function () {
    const messageBox = document.getElementById('popup-message');
    if (messageBox && messageBox.textContent.trim() !== "") {
        messageBox.classList.add('show');
        setTimeout(function () {
            messageBox.classList.remove('show');
            setTimeout(function () {
                messageBox.remove();
            }, 275);
        }, 2750);
    }
});