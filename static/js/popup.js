function showPopupMessage(message, messageType = 'success') {
    const popup = document.getElementById('popup-message');
    popup.textContent = message;

    popup.className = 'popup-message';

    switch (messageType) {
        case 'error':
            popup.classList.add('popup-message-error');
            break;
        case 'success':
            popup.classList.add('popup-message-success');
            break;
        case 'warning':
            popup.classList.add('popup-message-warning');
            break;
        case 'info':
            popup.classList.add('popup-message-info');
            break;
        case 'debug':
            popup.classList.add('popup-message-debug');
            break;
        default:
            popup.classList.add('popup-message-success');
    }

    if (message.trim() !== "") {
        popup.classList.add('show');
        setTimeout(() => {
            popup.classList.remove('show');
        }, 2500);
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
            }, 250);
        }, 2500);
    }
});