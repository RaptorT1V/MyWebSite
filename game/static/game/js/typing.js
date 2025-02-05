/*
===================================
    Инициализация констант
===================================
*/

const WORDS_EN = 'in one good real one not school set they state high life consider on and not come what also for set point can want as while with of order child about school thing never hold find order each too between program work end you home place around while place problem end begin interest while public or where see time those increase interest be give end think seem small as both another a child same eye you between way do who into again good fact than under very head become real possible some write know however late each that with because that place nation only for each change form consider we would interest with world so order or run more open that large write turn never over open each over change still old take hold need give by consider line only leave while what set up number part form want against great problem can because head so first this here would course become help year first end want both fact public long word down also long for without new turn against the because write seem line interest call not if line thing what work people way may old consider leave hold want life between most place may if go who need fact such program where which end off child down change to from people high during people find to however into small new general it do that could old for last get another hand much eye great no work and with but good there last think can around use like number never since world need what we around part show new come seem while some and since still small these you general which seem will place come order form how about just also they with state late use both early too lead general seem there point take general seem few out like might under if ask while such interest feel word right again how about system such between late want fact up problem stand new say move a lead small however large public out by eye here over so be way use like say people work for since interest so face order school good not most run problem group run she late other problem real form what just high no man do under would to each too end point give number child through so this large see get form also all those course to work during about he plan still so like down he look down where course at who plan way so since come against he all who at world because while so few last these mean take house who old way large no first too now off would in this course present order home public school back own little about he develop of do over help day house stand present another by few come that down last or use say take would each even govern play around back under some line think she even when from do real problem between long as there school do as mean to all on other good may from might call world thing life turn of he look last problem after get show want need thing old other during be again develop come from consider the now number say life interest to system only group world same state school one problem between for turn run at very against eye must go both still all a as so after play eye little be those should out after which these both much house become both school this he real and may mean time by real number other as feel at end ask plan come turn by all head increase he present increase use stand after see order lead than system here ask in of look point little too without each for both but right we come world much own set we right off long those stand go both but under now must real general then before with much those at no of we only back these person plan from run new as own take early just increase only look open follow get that on system the mean plan man over it possible if most late line would first without real hand say turn point small set at in system however to be home show new again come under because about show face child know person large program how over could thing from out world while nation stand part run have look what many system order some one program you great could write day do he any also where child late face eye run still again on by as call high the must by late little mean never another seem to leave because for day against public long number word about after much need open change also'.split(' ');
const WORDS_RU = 'и в не он на я что тот быть с а весь это как она по но они к у же из мы за да от я очень так для все она даже вот раз уже там сам чтобы без меня здесь нет быть мой до вы теперь в нее когда только вот уже можно при чем сейчас для себя еще все где-то где его было чем под после над мы про или ну что это другой такой через про между тут все это свой ни тоже тут кот дом солнце вода земля воздух человек друг работа город страна жизнь мир день ночь рука нога голова глаз ухо рот нос дерево цветок животное птица рыба зверь лес поле река море озеро гора небо звезда луна свет тьма огонь вода земля время год месяц неделя день час минута секунда утро вечер ночь день работа дом семья друг любовь счастье радость грусть страх гнев надежда мечта цель путь дорога путешествие приключение история книга фильм музыка песня танец искусство наука технология компьютер телефон интернет информация знание опыт умение навык сила слабость здоровье болезнь лечение врач больница лекарство еда вода напиток хлеб мясо рыба овощ фрукт молоко сыр масло сахар соль перец чай кофе вино пиво вода сок лимонад школа университет студент учитель урок задание экзамен оценка каникулы перемена класс доска мел тетрадь ручка карандаш линейка циркуль портфель рюкзак форма спорт футбол баскетбол волейбол теннис плавание бег прыжок удар гол очко матч игра команда игрок тренер судья победа поражение ничья результат счет время период тайм место позиция поле площадка корт бассейн стадион зал машина автобус трамвай троллейбус метро поезд самолет корабль велосипед мотоцикл дорога улица проспект площадь парк сквер аллея тропинка мост тоннель светофор переход остановка станция аэропорт вокзал порт магазин рынок супермаркет аптека банк почта офис завод фабрика предприятие организация фирма компания бизнес деньги рубль копейка доллар евро цена стоимость скидка товар услуга продажа покупка чек договор документ паспорт билет справка квитанция театр кино цирк музей выставка концерт спектакль представление артист художник музыкант певец танцор режиссер продюсер сцена занавес декорация костюм грим роль номер программа афиша билет место ряд балкон партер ложа одежда обувь платье брюки рубашка юбка пальто куртка шапка шарф перчатки носки колготки белье костюм пиджак галстук ремень сумка кошелек зонт очки часы украшение кольцо серьги цепочка браслет погода климат температура осадки ветер гроза дождь снег град туман облако радуга мороз жара тепло холод'.split(' ');
const GAME_TIME = 25 * 1000; // Время игры в миллисекундах
const CURSOR_TOP_OFFSET = '198px';
const CURSOR_LEFT_OFFSET = '100px';
const LINE_HEIGHT = 35;
const MAX_TOP_OFFSET = 260;

/*
===================================
    Инициализация переменных
===================================
*/

let currentLanguage = 'ru';
let currentWords = WORDS_RU;
let wordsCount = currentWords.length;
let timer = null;
let gameStart = null;


/*
===================================
    Вспомогательные функции
===================================
*/

function addClass(el, name) {
    el.classList.add(name);
}

function removeClass(el, name) {
    el.classList.remove(name);
}

function getRandomWord() {
    const randomIndex = Math.floor(Math.random() * currentWords.length);
    return currentWords[randomIndex];
}

function formatWord(word) {
    return `<div class="word"><span class="letter">${word.split('').join('</span><span class="letter">')}</span></div>`;
}

/*
===================================
    Функции управления игрой
===================================
*/

function toggleLanguage() {
    currentLanguage = currentLanguage === 'en' ? 'ru' : 'en';
    currentWords = currentLanguage === 'ru' ? WORDS_RU : WORDS_EN;
    wordsCount = currentWords.length;
    document.getElementById('langBtn').textContent = currentLanguage.toUpperCase();
}

function newGame() {
    const wordsContainer = document.getElementById('words');
    wordsContainer.innerHTML = '';
    for (let i = 0; i < 200; i++) {
        wordsContainer.innerHTML += formatWord(getRandomWord());
    }
    addClass(document.querySelector('.word'), 'current');
    addClass(document.querySelector('.letter'), 'current');
    document.getElementById('info').innerHTML = (GAME_TIME / 1000) + '';
    timer = null;
    removeClass(document.getElementById('game'), 'over');
}

function getWpm() {
    const words = [...document.querySelectorAll('.word')];
    const lastTypedWord = document.querySelector('.word.current');
    const lastTypedWordIndex = words.indexOf(lastTypedWord) + 1;
    const typedWords = words.slice(0, lastTypedWordIndex);
    const correctWords = typedWords.filter(word => {
        const letters = [...word.children];
        const incorrectLetters = letters.filter(letter => letter.classList.contains('incorrect'));
        const correctLetters = letters.filter(letter => letter.classList.contains('correct'));
        return incorrectLetters.length === 0 && correctLetters.length === letters.length;
    });
    return correctWords.length / GAME_TIME * 60000;
}

function gameOver() {
    clearInterval(timer);
    addClass(document.getElementById('game'), 'over');

    const result = getWpm();
    document.getElementById('info').innerHTML = `WPM: ${result}`;

    const roundedScore = Math.round(result);
    sendScore('typing', roundedScore);

    gameStart = null;

    const wordsContainer = document.getElementById('words');
    wordsContainer.style.marginTop = '0px';

    const cursorContainer = document.getElementById('cursor');
    cursorContainer.style.top = CURSOR_TOP_OFFSET;
    cursorContainer.style.left = CURSOR_LEFT_OFFSET;
}

function sendScore(gameName, score) {
    fetch('/game/save_score/', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'X-CSRFToken': getCookie('csrftoken')
      },
      body: 'game=' + encodeURIComponent(gameName) + '&score=' + encodeURIComponent(score)
    })
    .then(response => response.json())
    .then(data => {
    if (data.status === 'success') {
      console.log('Score saved successfully!');
    } else {
      console.error('Error saving score:', data.message);
    }
    })
    .catch(error => {
      console.error('Error:', error);
  });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Начинается ли эта строка cookie с нужного нам имени?
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

/*
===================================
    Обработчик событий клавиатуры
===================================
*/

document.getElementById('game').addEventListener('keyup', ev => {
    const key = ev.key;
    const currentWord = document.querySelector('.word.current');
    const currentLetter = document.querySelector('.letter.current');
    const expected = currentLetter?.innerHTML || ' ';
    const isLetter = key.length === 1 && key !== ' ';
    const isSpace = key === ' ';
    const isBackspace = key === 'Backspace';
    const isFirstLetter = currentLetter === currentWord.firstChild;

    if (document.querySelector('#game.over')) {
        return;
    }

    if (!timer && isLetter) {
        timer = setInterval(() => {
            if (!gameStart) {
                gameStart = Date.now();
            }
            const currentTime = Date.now();
            const msPassed = currentTime - gameStart;
            const sPassed = Math.round(msPassed / 1000);
            const sLeft = Math.round((GAME_TIME / 1000) - sPassed);
            if (sLeft <= 0) {
                gameOver();
                return;
            }
            document.getElementById('info').innerHTML = sLeft + '';
        }, 1000);
    }

    if (isLetter) {
        if (currentLetter) {
            addClass(currentLetter, key === expected ? 'correct' : 'incorrect');
            removeClass(currentLetter, 'current');
            if (currentLetter.nextSibling) {
                addClass(currentLetter.nextSibling, 'current');
            }
        } else {
            const incorrectLetter = document.createElement('span');
            incorrectLetter.innerHTML = key;
            incorrectLetter.className = 'letter incorrect extra';
            currentWord.appendChild(incorrectLetter);
        }
    }

    if (isSpace) {
        if (expected !== ' ') {
            const lettersToInvalidate = [...document.querySelectorAll('.word.current .letter:not(.correct)')];
            lettersToInvalidate.forEach(letter => {
                addClass(letter, 'incorrect');
            });
        }

        const extraLetters = currentWord.querySelectorAll('.letter.extra');
        extraLetters.forEach(letter => currentWord.removeChild(letter));

        removeClass(currentWord, 'current');
        addClass(currentWord.nextSibling, 'current');

        if (currentLetter) {
            removeClass(currentLetter, 'current');
        }
        if (currentWord.nextSibling) {
            addClass(currentWord.nextSibling.firstChild, 'current');
        }
    }

    if (isBackspace) {
        if (currentLetter && isFirstLetter && currentWord.previousSibling) {
            removeClass(currentWord, 'current');
            addClass(currentWord.previousSibling, 'current');
            removeClass(currentLetter, 'current');
            addClass(currentWord.previousSibling.lastChild, 'current');
            removeClass(currentWord.previousSibling.lastChild, 'incorrect');
            removeClass(currentWord.previousSibling.lastChild, 'correct');
        } else if (currentLetter && !isFirstLetter) {
            removeClass(currentLetter, 'current');
            addClass(currentLetter.previousSibling, 'current');
            removeClass(currentLetter.previousSibling, 'incorrect');
            removeClass(currentLetter.previousSibling, 'correct');
        } else {
            const extraLetters = currentWord.querySelectorAll('.letter.extra');
            if (extraLetters.length > 0) {
                currentWord.removeChild(extraLetters[extraLetters.length - 1]);
            } else {
                addClass(currentWord.lastChild, 'current');
                removeClass(currentWord.lastChild, 'incorrect');
                removeClass(currentWord.lastChild, 'correct');
            }
        }
    }

    // Перемещение строк
    if (currentWord.getBoundingClientRect().top > MAX_TOP_OFFSET) {
        const currentWords = document.getElementById('words');
        const margin = parseInt(currentWords.style.marginTop || '0px');
        currentWords.style.marginTop = (margin - LINE_HEIGHT) + 'px';
    }

    // Перемещение курсора
    const nextLetter = document.querySelector('.letter.current');
    const nextWord = document.querySelector('.word.current');
    const cursor = document.getElementById('cursor');
    cursor.style.top = (nextLetter || nextWord).getBoundingClientRect().top + 2 + 'px';
    cursor.style.left = (nextLetter || nextWord).getBoundingClientRect()[nextLetter ? 'left' : 'right'] + 'px';
});

/*
===================================
    Обработчики кнопок
===================================
*/

document.getElementById('newGameBtn').addEventListener('click', () => {
    gameOver();
    removeClass(document.getElementById('game'), 'over');
    newGame();
});

document.getElementById('langBtn').addEventListener('click', () => {
    toggleLanguage();
    gameOver();
    removeClass(document.getElementById('game'), 'over');
    newGame();
});


/*
===================================
    Инициализация игры
===================================
*/

newGame();