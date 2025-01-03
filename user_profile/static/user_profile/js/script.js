// Скрытие и показ формы смены пароля
document.addEventListener('DOMContentLoaded', function() {
    const showPasswordBtn = document.getElementById('show-password-modal');
    const formContainer = document.getElementById('password-modal');

    if (showPasswordBtn && formContainer) {
        showPasswordBtn.addEventListener('click', function() {
            formContainer.style.display = (formContainer.style.display === 'none' || formContainer.style.display === '') ? 'block' : 'none';
        });
    }

    // Логика закрытия модального окна
    const closeBtn = document.querySelector('#password-modal .close');
    if (closeBtn) {
        closeBtn.addEventListener('click', function() {
            formContainer.style.display = 'none';
        });
    }
});


// Lightbox
function openLightbox(imageSrc) {
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    lightboxImg.src = imageSrc;
    lightbox.style.display = 'block';
}

// Закрытие Lightbox
document.getElementById('lightbox').addEventListener('click', function() {
    this.style.display = 'none';
});