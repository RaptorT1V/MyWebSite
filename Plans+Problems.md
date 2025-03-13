# Визуальное отображение страницы с продуктами

## Должен быть значок корзины слева от имени пользователя

## Расширить вширь (не по 2 товара, а по 4; как в нечётных номерах)

## Страницы с товарами. Сколько умещается на одну? (добавить больше товаров)

## Анимация точки (работающие примеры)

## Покрас формы, в которой находится кнопка

- - - - - - - - - - - - - - - - - - - -
# Страница с корзиной
Придумаем, что тут сделать

## Ошибка добавления в корзину
- - - - - - - - - - - - - - - - - - - -
# Страница карточки товара

## Пикча должна иметь строгий размер (также для похожих товаров)

## Блок с похожими товарами

- - - - - - - - - - - - - - - - - - - -
Как посмотреть историю заказов у пользователя? И сам заказ?
Куда будут отправляться деньги? Админу?
- - - - - - - - - - - - - - - - - - - -
# Исправления для админки (файл models.py --> class Product)

## Уникальные поля (в зависимости от категории)

В зависимости от выбранной категории сделать различные уникальные поля.
Например, для одежды важен размер, цвет и всякие другие параметры.
Для аксессуаров важен вес, цвет
Для музыки, например, год издания, вес, продолжительность пластинки и так далее

## Цены со скидкой может и не быть. + Визуальное отображение скидки
Сделать так, чтобы можно было не выбирать цену со скидкой.

И сделать так, чтобы, если скидка есть, показывалась старая цена, но в зачёркнутом виде и типа где-то в углу или рядом.
- - - - - - - - - - - - - - - - - - - -
# То, что мне понравилось (дизайн страницы с продуктами)
Номера: 0, 2, 5, 6, 8, 10, 12, 14, 16, 18 – узкое расположение (по 2 в ширину) + строка поиска находится в одной форме с товарами
Номера: 1, 3, 4, 7, 9, 11, 13, 15, 17, 19 – широкое расположение (по 4 в ширину) + строка поиска находится вне формы с товарами (отдельно сверху)

Плохие варианты: 0, 3, 5, 11, 13, 14,
Норм варианты: 1, 2, 4, 6, 8, 10, 16, 18, 19
Супер варианты: 7, 9, 12, 15, 17
    Одобренные: 1, 2, 15, 17
- - - - - - - - - - - - - - - - - - - -
# Добавить комменты в project_structure.txt

# № last – Check Refactoring (html, css, js)
- - - - - - - - - - - - - - - - - - - -
# № ? – Доделать магазин !
Хотя бы на базовом уровне

# № ? – Делать форум или нет? 

# № ? – Делать ли личные сообщения?
Личные сообщения тоже как идея интересная. 
Потому что уже есть задел: в game можно тыкнуть на имя профиля и перейти на его страницу.
__________________________________________________________________________

    --> NEVER REALISED <--

# Это точно нужно!


## Функционал

### №1 – Перемотка трека на странице musician_resume.html
Я навожу мышкой на прогресс-бар и мне даже показывается время, соответствующее тому месту прогресс-бара, на которое я навёл мышкой.
Но вот когда я нажимаю ЛКМ на любое место прогресс-бара у меня песня заново начинает играть. Вместо перемотки.
Я мучался с этой проблемой очень долго!

Я попробовал загрузить несколько треков небольшой длины.
Также я попробовал конвертировать WAV в MP3.
И вот какие выводы я сделал.

1. Короткие треки (максимум 1 минута) не перематываются, а перезагружаются. Но есть один нюанс. Если их прослушать полностью (от начала и до конца) и воспроизвести заново, то они БУДУТ перематываться.
И пока ты не перезагрузишь страницу у тебя будут перематываться они.

То есть, сначала у меня загрузился трек. Я не смог его перематывать. 
Потом трек дошёл до конца. Включился новый. 
Я включил предыдущий и попробовал перемотать ещё раз. Всё получилось.

А ещё у меня был такой баг, что я загрузил 2 коротких трека. Прослушал только один. А потом после обновления у меня первый перестал перематываться, а второй сразу же перематывался.
И вот этот второй трек он навечно в памяти сохранился. Он всегда теперь перематывается, лол. А остальные сбрасываются после перезагрузки страницы.
И ещё один трек такой попался, который сразу перематывался.

2. Длинные треки (3 минуты) не перематываются, даже если их прослушать полностью. Они так и будут перезагружаться при перемотке.

3. Нет разницы: mp3 или wav. Самое главное -- это длительность трека.

Причём я установил опытным путём, что короткими треками точно считаются треки, длительность которых от 1 до 62 секунд. То есть после проигрывания до конца такие треки получают способность перематываться.
Треки с длительностью в диапазоне от 63 секунд до 74 секунд -- я не знаю ничего про них. У меня нет таких треков. Но есть трек на 75 секунд.
И вот уже трек длительностью от 75 секунды 100% считается длинным и после его проигрывания до конца он всё равно НЕ получает способность перематываться.
Я не знаю, с чем связана эта особенность.


## Дизайн

### №1 – Две связанные друг с другом проблемы: масштабирование и позиционирование. 
Я решил её для всех страниц (main.css), кроме musician_resume.html. 
Я не знаю, почему там не хочет она фикситься.

UPD: Как оказалось, эта проблема не только там не хочет фикситься...

Белые прямоугольники при масштабировании появляются. Я хз, что это. 
Но они появляются только если прям масштабировать сильно страницу. А именно **когда хотя бы один из элементов не помещается на странице** (выходит за рамки).
Тогда возникает белый такой прямоугольник, который вытянут по вертикали и идёт по всему body от \<body\> до \</body\>

~~Я думаю, проблему нужно искать в main.css.~~

### №2 – Неправильное расположение avatar-overlay в profile.html других юзеров
Когда ты смотришь профиль другого человека, у тебя доступен только один значок -- лупы (посмотреть аватарку).
Из-за того, что позиционирование абсолютное, а значков становится не 3, а 1, такая фигня и получается. Круг этот чёрный вылезает за рамки аватарки. И очень уж сильно.
Причём, такое ощущение, что это всё зависит от длины никнейма пользователя. То есть, чем длиннее username, тем ужаснее становится выпячивание этого чёрного круга.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# А точно ли это нужно?


## Функционал

### №1 – Вариативность входа
В login.html сделать поле "username_or_email" вместо поля "username". 
<br> Чтобы в аккаунт можно было зайти либо через комбинацию "логин + пароль", либо через комбинацию "e-mail + пароль".

### №2 – Когда меняешь пароль и ошибаешься
Я больше НЕ хочу нажимать на кнопку "сменить пароль" КАЖДЫЙ РАЗ, когда ошибаюсь, чтобы эта форма опять отобразилась и я смог снова попытаться сменить пароль!
<br> Дело в том, что каждый раз, когда возникает ошибка, страница перезагружается и форма скрывается. И поэтому мне приходится каждый раз нажимать на кнопку "Change Password", чтобы сменить пароль.
<br> А хочется, чтобы после того, как ты ошибся, форма оставалась открытой!

### №3 – Можно зайти в игру без регистрации
Это хорошо или плохо?
Если человек знает url, он может спокойно зайти в игру, обойдя регистрацию.
Правда что он может ей сделать? Если счёт всё равно не запишется.


## Дизайн

### №1 – Дизайн profile.html.
1. Форма смены пароля должна находиться по центру и быть чуточку поменьше. ~~Чтобы влезала на масштабе 125%.~~
2. В целом, форма выглядит довольно в старом стиле. Надо добавить крутых стилей!

### №2 – Какая-то дичь с отступами в programmer_resume.html
Особенно настораживает секция с pdf и секция с сертификатами.
Когда увеличиваешь масштаб, какая-то странная фигня происходит.

### №3 – Постепенное "очёрнобеливание" обложки musician_resume.html
Чем ближе громкость к нулю, тем меньше насыщенности должно быть у обложки.

### №4 – Визуализатор музыкальной дорожки на странице musician_resume.html
Он просто должен выглядеть красивее и аккуратнее.

### №6 – Разукрасить магнетизм на странице home.html
Когда буквы притягиваются они должны ещё и светиться с той стороны, где курсор. 
Таким образом у гравитации появится источник света как бы. То есть курсор и будет источником света (как в Blender)

### №6 – Курсор должен меняться на красный (aim2.png) при зажатии ЛКМ в любой точке <div class="main-content-custom"> на странице home.html
А сейчас пока только в области gravity-text

### №7 – Доп. стили для forum

#### 1-ый вариант
```html
{% extends 'base.html' %}
{% load static %}

{% block title %}Форум{% endblock %}

{% block extra_css %}
<link rel="stylesheet" href="{% static 'forum/css/style.css' %}">
{% endblock %}

{% block content %}
<div class="coming-soon magic-portal-variation">
  <img src="{% static 'forum/img/galaxy-background2.jfif' %}" alt="Фэнтезийный фон" class="magic-bg">

  <div class="portal-scene">
    <div class="portal">
      <div class="portal-ring ring-outer"></div>
      <div class="portal-ring ring-middle"></div>
      <div class="portal-ring ring-inner"></div>
      <img src="{% static 'forum/img/under-construction.png' %}" alt="Ведутся работы" class="construction-image">
    </div>
  </div>

  <h1 id="dynamic-title"></h1>
  <p>Вот-вот врата откроются...</p>
  <div id="timer">Время до запуска: <span id="countdown"></span></div>
</div>
{% endblock %}

{% block extra_js %}
<script src="{% static 'forum/js/script.js' %}"></script>
{% endblock %}
```

```css
/* 
  Общий контейнер
  Используем фантазийный/декоративный шрифт и делаем позиционирование 
*/
.magic-portal-variation {
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: 'Cinzel Decorative', cursive;
  color: #fff;
  overflow: hidden;
}

/* Фоновое изображение */
.magic-portal-variation .magic-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 1;
  filter: brightness(0.5) blur(2px);
}

/* Основная сцена портала, даём ей перспективу */
.portal-scene {
  position: relative;
  width: 100%;
  height: 450px;
  display: flex;
  align-items: center;
  justify-content: center;
  perspective: 1200px;  /* для 3D */
  z-index: 2;
}

/* Контейнер самого портала */
.portal {
  position: relative;
  width: 300px; 
  height: 300px;
  transform-style: preserve-3d;
  animation: portalPulse 6s infinite ease-in-out; 
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Анимация "пульсации" портала (масштаба) */
@keyframes portalPulse {
  0%, 100% {
    transform: scale(1) rotateY(0deg);
  }
  50% {
    transform: scale(1.05) rotateY(180deg);
  }
}

/* Общие для колец портала (слои) */
.portal-ring {
  position: absolute;
  border-radius: 50%;
  transform-style: preserve-3d;
  box-shadow: 0 0 30px rgba(255,255,255,0.7), inset 0 0 40px rgba(255,255,255,0.5);
  animation: rotatePortal 8s linear infinite;
  opacity: 0.9;
}

/* Анимация вращения каждого кольца */
@keyframes rotatePortal {
  0% {
    transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg);
  }
  100% {
    transform: rotateX(360deg) rotateY(360deg) rotateZ(360deg);
  }
}

.ring-outer {
  width: 300px;
  height: 300px;
  background: conic-gradient(
    from 0deg,
    rgba(255, 215, 0, 0.3),
    rgba(255, 140, 0, 0.6),
    rgba(255, 215, 0, 0.3),
    rgba(255, 140, 0, 0.6),
    rgba(255, 215, 0, 0.3)
  );
}

.ring-middle {
  width: 220px;
  height: 220px;
  background: conic-gradient(
    from 90deg,
    rgba(255, 0, 255, 0.5),
    rgba(255, 140, 0, 0.3),
    rgba(255, 0, 255, 0.5),
    rgba(255, 140, 0, 0.3)
  );
}

.ring-inner {
  width: 140px;
  height: 140px;
  background: conic-gradient(
    from 180deg,
    rgba(0, 255, 255, 0.6),
    rgba(255, 215, 0, 0.4),
    rgba(0, 255, 255, 0.6),
    rgba(255, 215, 0, 0.4)
  );
}

/* Картинка "Ведутся работы" в центре портала */
.construction-image {
  width: 100px;
  transform: translateZ(50px); /* выносим вперёд из центра кольца */
  animation: fadeInPortal 4s forwards ease;
  opacity: 0; /* изначально невидим */
}

/* Плавное "проявление" */
@keyframes fadeInPortal {
  0% {
    opacity: 0;
    transform: scale(0) translateZ(50px);
  }
  100% {
    opacity: 1;
    transform: scale(1) translateZ(50px);
  }
}

/* Заголовок */
.magic-portal-variation h1 {
  z-index: 3;
  margin-top: 2rem;
  font-size: 2rem;
  text-shadow: 0 0 8px rgba(255,255,255,0.8);
  animation: fadeInTitle 2s ease forwards;
  opacity: 0;
}
@keyframes fadeInTitle {
  to {
    opacity: 1;
  }
}

/* Подпись */
.magic-portal-variation p {
  z-index: 3;
  margin-top: 1rem;
  font-size: 1.4rem;
  text-shadow: 0 0 5px rgba(255,255,255,0.6);
}

/* Таймер */
.magic-portal-variation #timer {
  z-index: 3;
  margin-top: 1rem;
  font-size: 1.6rem;
  font-weight: bold;
  text-shadow: 0 0 5px rgba(255,255,255,0.9);
}

/* Цифры таймера меняют цвет */
.magic-portal-variation #countdown {
  animation: colorShift 3s infinite;
}
@keyframes colorShift {
  0%   { color: #0ff; }
  25%  { color: #ff0; }
  50%  { color: #f0f; }
  75%  { color: #adff2f; }
  100% { color: #0ff; }
}

/* 
  Дополнительный динамический эффект "волшебной волны".
  Реализуем псевдоэлемент на .magic-portal-variation::after 
*/
.magic-portal-variation::after {
  content: "";
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(255,255,255,0.15), transparent 70%);
  animation: waveMove 12s linear infinite;
  z-index: 1;
}
@keyframes waveMove {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

/* Адаптивность */
@media (max-width: 600px) {
  .portal-scene {
    height: 300px;
  }
  .portal {
    width: 200px;
    height: 200px;
  }
  .ring-outer {
    width: 200px;
    height: 200px;
  }
  .ring-middle {
    width: 140px;
    height: 140px;
  }
  .ring-inner {
    width: 80px;
    height: 80px;
  }
  .construction-image {
    width: 60px;
  }
  .magic-portal-variation h1 {
    font-size: 1.6rem;
  }
  .magic-portal-variation p,
  .magic-portal-variation #timer {
    font-size: 1.2rem;
  }
}
```

```js
// Установка даты запуска форума
const launchDate = new Date("2025-04-29T12:00:00Z");

// Эффект "печатающей машинки" для заголовка
const dynamicTitle = document.getElementById("dynamic-title");
const titleText = "Откройте магический портал на наш форум!";
let i = 0;

function typeWriterMagicPortal() {
  if (i < titleText.length) {
    dynamicTitle.innerHTML += titleText.charAt(i);
    i++;
    setTimeout(typeWriterMagicPortal, 100);
  }
}
typeWriterMagicPortal();

// Таймер обратного отсчёта
function updateCountdownMagicPortal() {
  const now = new Date();
  const diff = launchDate - now;
  const countdownEl = document.getElementById("countdown");

  if (diff < 0) {
    countdownEl.textContent = "Форум запущен!";
    return;
  }

  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
  const minutes = Math.floor((diff / (1000 * 60)) % 60);
  const seconds = Math.floor((diff / 1000) % 60);

  countdownEl.textContent = `${days}д ${hours}ч ${minutes}м ${seconds}с`;
}

setInterval(updateCountdownMagicPortal, 1000);
updateCountdownMagicPortal();

// Дополнительный 3D-эффект для колец портала при движении мыши
const portalRings = document.querySelectorAll('.portal-ring');
const portalContainer = document.querySelector('.portal');

document.addEventListener('mousemove', (e) => {
  // Для определения центра экрана
  const centerX = window.innerWidth / 2;
  const centerY = window.innerHeight / 2;
  // Смещение мыши
  const offsetX = (e.clientX - centerX) / 30;
  const offsetY = (e.clientY - centerY) / 30;

  portalRings.forEach((ring, i) => {
    // Индекс для постепенного усиления эффекта
    const depth = (i + 1) * 5;
    ring.style.transform = `
      rotateX(${offsetY * depth}deg) 
      rotateY(${offsetX * depth}deg) 
      rotateZ(0deg)
    `;
  });
});
```

#### 2-ой вариант
```html
{% extends 'base.html' %}
{% load static %}

{% block title %}Форум{%endblock %}

{% block extra_css %}
<link rel="stylesheet" type="text/css" href="{% static 'forum/css/style.css' %}">
{% endblock %}

{% block content %}
<div class="coming-soon big-variation portal-theme">
  <div class="portal-container">
    <div class="portal-bg"></div>
    <div class="portal-rings">
      <div class="portal-ring"></div>
      <div class="portal-ring"></div>
      <div class="portal-ring"></div>
    </div>
    <div class="portal-center">
      <img src="{% static 'forum/img/under-construction.png' %}" alt="Ведутся работы" class="construction-image">
    </div>
    <div class="portal-glow"></div>
  </div>
  <div class="portal-text">
      <h1 id="dynamic-title"></h1>
      <p>портал откроется...</p>
        <div id="timer">
          через: <span id="countdown"></span>
       </div>
  </div>
</div>
{% endblock %}

{% block extra_js %}
    <script src="{% static 'forum/js/script.js' %}"></script>
{% endblock %}
```

```css
body {
    overflow: hidden;
    margin: 0;
    font-family: 'Philosopher', sans-serif; /* "Магический" шрифт с засечками */
    background-color: #0d0d1a; /* Темно-фиолетовый фон */
    color: #eee;
}

.coming-soon.big-variation.portal-theme {
  position: relative;
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

/* Контейнер портала (для удобства позиционирования) */
.portal-container {
    position: relative;
    width: 300px;
    height: 300px;
    margin-bottom: 2em;
    perspective: 800px; /* Добавляем перспективу для 3D-эффекта */

}

/* Фон портала (мерцающие частицы) */
.portal-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(ellipse at center, rgba(153, 50, 204, 0.3) 0%, rgba(0, 0, 0, 0) 70%);
    border-radius: 50%;
    animation: shimmer-bg 5s linear infinite;
    z-index: 0;
}

@keyframes shimmer-bg {
    0% {
        filter: hue-rotate(0deg);
    }
    100% {
        filter: hue-rotate(360deg); /* Меняем цвета фона */
    }
}

/* Кольца портала */
.portal-rings {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
}

.portal-ring {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) rotate(0deg); /* Начальный поворот */
    border-radius: 50%;
    border: 2px solid transparent; /* Прозрачная основа */
    mix-blend-mode: screen;  /* Режим смешивания для свечения */

}
.portal-ring:nth-child(1) {
    width: 100%;
    height: 100%;
    border-image: linear-gradient(to bottom, #9932CC, #DA70D6) 1; /* Градиент */
    box-shadow: 0 0 20px 5px #9932CC;
    animation: rotate 8s linear infinite, pulse-ring 5s ease-in-out infinite alternate;

}
.portal-ring:nth-child(2) {
    width: 80%;
    height: 80%;
     border-image: linear-gradient(to bottom, #DA70D6, #FF00FF) 1;
    box-shadow: 0 0 15px 3px #DA70D6;
     animation: rotate 6s linear reverse infinite, pulse-ring 4s ease-in-out infinite alternate;

}

.portal-ring:nth-child(3) {
    width: 60%;
    height: 60%;
     border-image: linear-gradient(to bottom, #FF00FF, #fff) 1;
    box-shadow: 0 0 10px 2px #FF00FF;
    animation: rotate 4s linear infinite, pulse-ring 3s ease-in-out infinite alternate;

}

@keyframes rotate {
    from {
        transform: translate(-50%, -50%) rotate(0deg);
    }
    to {
        transform: translate(-50%, -50%) rotate(360deg);
    }
}
@keyframes pulse-ring {
  from {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0.8;
  }
  to {
    transform: translate(-50%, -50%) scale(1.1);
    opacity: 1;
  }
}

/* Центр портала (где появляется изображение) */
.portal-center {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0); /* Изначально скрыт */
    width: 80%;
    height: 80%;
    border-radius: 50%;
    background-color: rgba(0, 0, 0, 0.7);
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 2;
    transition: transform 0.5s ease; /* Плавное появление */
     animation: portalOpen 3s ease-out forwards;
}
@keyframes portalOpen{
  0%{
    transform: translate(-50%, -50%) scale(0);
        opacity: 0;
  }
  80%{
     transform: translate(-50%, -50%) scale(1.2); /* Небольшое увеличение */
        opacity: 1;
  }
  100%{
     transform: translate(-50%, -50%) scale(1);
        opacity: 1;
  }
}
/* Свечение вокруг портала */
.portal-glow {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 110%;
    height: 110%;
    border-radius: 50%;
    background: radial-gradient(ellipse at center, rgba(255, 255, 255, 0.2) 0%, rgba(0, 0, 0, 0) 70%);
    filter: blur(20px); /* Размытие для мягкого свечения */
    z-index: -1; /* За порталом */
    animation: pulse-glow 4s ease-in-out infinite alternate;
}

@keyframes pulse-glow {
  from {
    opacity: 0.5;
  }
  to {
    opacity: 1;
  }
}

/* Изображение */
.portal-theme .construction-image {
    width: 80%;
    height: auto;
    filter: drop-shadow(0 0 1rem #fff); /* Белое свечение */
     transition: transform 0.3s ease;
}
.portal-container:hover .construction-image{
   filter: drop-shadow(0 0 1.5rem #b19cd9);
}

/* Текст */
.portal-text {
    position: relative;
    z-index: 3; /* Над порталом */
    text-align: center;
     margin-top: 1em;
}

.portal-theme h1 {
  font-size: 3em;
  margin: 0;
    margin-bottom: 0.3em;
  color: #fff;
  text-shadow: 0 0 15px #b19cd9; /* Светло-фиолетовое свечение */
    animation: pulsate 2s ease-in-out infinite alternate;
}
@keyframes pulsate {
    from {
        text-shadow: 0 0 15px #b19cd9;
    }
    to {
        text-shadow: 0 0 25px #b19cd9, 0 0 35px #8e44ad;
    }
}

.portal-theme p {
    font-size: 1.5em;
  color: #ccc;
    margin-bottom: 0.5em;
    text-shadow: 0 0 5px rgba(204, 204, 204, 0.8);
}

.portal-theme #timer {
  font-size: 2em;
  color: #eee;
    margin-top: 0.5em;
  text-shadow: 0 0 10px #b19cd9;
}
```

```js
// Дата запуска
const launchDate = new Date("2025-04-29T12:00:00Z");

// Эффект "набора текста по буквам" для заголовка
const dynamicTitle = document.getElementById("dynamic-title");
const titleText = "Форум скоро откроется!";
let letterIndex = 0;

function typeText() {
    if (letterIndex < titleText.length) {
        dynamicTitle.textContent += titleText[letterIndex];
        letterIndex++;
        setTimeout(typeText, 75); // Скорость набора
    }
}

typeText();

// Функция обновления таймера (стандартная)
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
    document.getElementById("countdown").innerHTML = "Портал открыт!";
  }
}

const countdownInterval = setInterval(updateCountdown, 1000);
updateCountdown();

// Интерактивность: меняем свечение при наведении на портал
const portalContainer = document.querySelector(".portal-container");
const portalRings = document.querySelectorAll(".portal-ring");

portalContainer.addEventListener("mouseenter", () => {
  portalRings.forEach(ring => {
    ring.style.filter = "brightness(1.5)"; // Увеличиваем яркость
  });
    // Добавляем более интенсивное свечение
});

portalContainer.addEventListener("mouseleave", () => {
  portalRings.forEach(ring => {
     ring.style.filter = "brightness(1)";
  });

});
```

## Игры

### Snake
1. Увеличить площадь поля (соответственно, и количество квадратиков).
2. Увеличить масштаб

Площадь поля изменить несложно. Достаточно изменить параметры  ```this.dimLong = 28; this.dimShort = 16;```
Но вот масштаб при этом уменьшается. То есть, проще говоря, всё мельче становится. Хрен разглядишь зелёный квадратик и змейку (особенно в начале, когда она маленькая)

### Ninja
1. Добавить win-streak. 
То есть, когда ты идеально попадаешь несколько раз подряд в красную точку у тебя не +2 прибавляется каждый раз, а +3, +4 и так далее...

### Typing
Ввести расчёт CPM? Чтобы был не только WPM.
Но тогда придётся и видоизменять таблицу рейтинга.