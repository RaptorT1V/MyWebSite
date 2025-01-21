// Дата запуска (можно не менять)
const launchDate = new Date("2025-06-29T12:00:00Z");

// Эффект "бегущей строки" для заголовка
const dynamicTitle = document.getElementById("dynamic-title");
const titleText = "Форум скоро откроется!";
let currentIndex = 0;
let direction = 1; // 1 - вправо, -1 - влево

function runningText() {
    let displayedText = titleText.substring(currentIndex) + " " + titleText.substring(0, currentIndex);
    dynamicTitle.innerText = displayedText;

    currentIndex += direction;
    if (currentIndex >= titleText.length || currentIndex <= 0) {
        direction *= -1; // Меняем направление
    }

    setTimeout(runningText, 150); // Скорость "бега"
}

runningText(); // Запуск эффекта


// Функция обновления таймера (обычная)
function updateCountdown() {
    const now = new Date();
    const diff = launchDate.getTime() - now.getTime();

    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((diff % (1000 * 60)) / 1000);

  document.getElementById("countdown").innerHTML = `${days}д ${hours}ч ${minutes}м ${seconds}с`;

    if (diff < 0) {
        clearInterval(countdownInterval);
        document.getElementById("countdown").innerHTML = "Форум запущен!";
    }
}
// Обновление таймера каждую секунду
const countdownInterval = setInterval(updateCountdown, 1000);
updateCountdown();

// Интерактивная тень для изображения (более выраженная)
const constructionImage = document.querySelector(".cyberpunk-theme .construction-image");

document.addEventListener("mousemove", (e) => {
  const x = e.clientX / window.innerWidth;
  const y = e.clientY / window.innerHeight;
  const shadowX = (x - 0.5) * 80; // Еще сильнее реагирует
  const shadowY = (y - 0.5) * 80;
  //  добавляем цветную тень
  constructionImage.style.boxShadow = `${shadowX}px ${shadowY}px 25px rgba(0, 255, 255, 0.6)`;
    constructionImage.style.transform = `perspective(500px) rotateY(${(x - 0.5) * 30}deg) rotateX(${(0.5 - y) * 30}deg)`;

});