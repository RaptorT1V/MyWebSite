// пришлось добавить эту строчку, чтобы код с вызовом showPopupMessage() выполнялся только после полной загрузки документа, иначе не будет работать

document.addEventListener('DOMContentLoaded', function() {
    {% if form.errors %}
    showPopupMessage("Ты даже не можешь войти? What a shame!", 'error');
    {% endif %}
});