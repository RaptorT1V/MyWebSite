/*
==========================================================
     Инициализация переменных для управления плеером
==========================================================
*/

let currentTrackIndex = 0;       // Индекс текущего трека
let audioContext, analyser, bufferLength, dataArray, source; // Аудио контекст | Анализатор для визуализации | Размер буфера анализатора | Массив данных анализатора | Источник аудио
let initialY, initialVolume;     // Запоминаем, где нажали (для изменения громкости) | Запоминаем текущую громкость
let isMouseDownOnCover = false;  // Флаг, нажата ли мышь на обложке

const audioPlayer = document.getElementById('audio-player'); // Элемент audio
const playPauseBtn = document.getElementById('play-pause');  // Кнопка play/pause
const prevBtn = document.getElementById('prev-track');       // Кнопка предыдущего трека
const nextBtn = document.getElementById('next-track');       // Кнопка следующего трека
const progressBar = document.querySelector('.progress');     // Прогресс-бар
const progressBarContainer = document.querySelector('.progress-bar'); // Прогресс-бар контейнер
const currentTimeSpan = document.getElementById('current-time');      // Текущее время
const durationSpan = document.getElementById('duration');    // Общая продолжительность
const albumCover = document.getElementById('cover-art');     // Обложка альбома
const trackTitle = document.getElementById('track-title');   // Название трека
const trackArtist = document.getElementById('track-artist'); // Имя исполнителя


/*
===========================================
     Создание элементов и DOM-структуры
===========================================
*/

// Создаём canvas для визуализации аудио
const canvas = document.createElement('canvas');
canvas.className = 'visualizer';
const ctx = canvas.getContext('2d');

// Добавляем canvas в DOM
document.querySelector('.player-content').insertBefore(
    canvas,
    document.querySelector('.track-info')
);
canvas.classList.add('visualizer-behind');

// Создаём tooltip для прогресс-бара
const tooltip = document.createElement('div');
tooltip.classList.add('progress-tooltip');
progressBarContainer.appendChild(tooltip);


/*
===================================
   Функции для управления плеером
===================================
*/

// Функция загрузки трека
function loadTrack(trackIndex) {
    console.log('=== LoadTrack ===');
    console.log('Loading track index:', trackIndex);

    const track = tracks[trackIndex];
    console.log('Track data:', track);

    audioPlayer.src = track.url;
    console.log('Set audio source:', audioPlayer.src);
    albumCover.src = track.cover;
    trackTitle.textContent = track.title;
    trackArtist.textContent = track.artist;

    audioPlayer.load();
    console.log('Audio player loaded');

    // Обновляем цвет фона плеера на основе обложки
    const img = new Image();
    img.crossOrigin = "Anonymous";
    img.src = track.cover;
    img.onload = function() {
        const color = getAverageColor(img);
        document.querySelector('.music-player').style.background =
            `linear-gradient(145deg, ${color}, ${adjustColor(color, -30)})`;
    }
}

// Функция форматирования времени
function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    seconds = Math.floor(seconds % 60);
    return `${minutes}:${seconds.toString().padStart(2, '0')}`;
}

// Функция креативной регулировки громкости
function updateVolumeVisual(volume) {
    const indicator = document.querySelector('.volume-indicator');
    const circle = document.querySelector('.volume-circle');
    const percentage = document.querySelector('.volume-percentage');
    const albumCover = document.querySelector('.album-cover');

    if (indicator) {
        indicator.style.display = isMouseDownOnCover ? 'block' : 'none';
    }

    if (circle && percentage) {
        circle.style.height = `${volume * 100}%`;
        percentage.textContent = `${Math.round(volume * 100)}%`;
    }

    // Применяем ч/б фильтр если громкость = 0
    if (albumCover) {
        albumCover.classList.toggle('muted', volume === 0);
    }
}


/*
==========================
   Функции визуализации
==========================
*/

// Функция обновления визуализатора
function updateVisualizer() {
    requestAnimationFrame(updateVisualizer);

    analyser.getByteFrequencyData(dataArray);

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    const radius = Math.min(centerX, centerY) - 10;

    // Пытаемся сместить начало круга, чтобы не было заметно, где старт
    const startAngle = -Math.PI / 2;
    const angleStep = (2 * Math.PI) / bufferLength;

    ctx.beginPath();
    for (let i = 0; i < bufferLength; i++) {
        const angle = startAngle + i * angleStep;
        const amplitude = dataArray[i] / 255;
        const x = centerX + (radius + amplitude * 50) * Math.cos(angle);
        const y = centerY + (radius + amplitude * 50) * Math.sin(angle);

        if (i === 0) {
            ctx.moveTo(x, y);
        } else {
            ctx.lineTo(x, y);
        }
    }
    ctx.closePath();

    // Заливаем градиентом
    const gradient = ctx.createRadialGradient(centerX, centerY, radius * 0.3, centerX, centerY, radius + 50);
    gradient.addColorStop(0, 'rgba(255, 0, 0, 0.5)');
    gradient.addColorStop(0.33, 'rgba(0, 255, 0, 0.5)');
    gradient.addColorStop(0.66, 'rgba(0, 0, 255, 0.5)');
    gradient.addColorStop(1, 'rgba(255, 255, 0, 0.5)');
    ctx.fillStyle = gradient;
    ctx.fill();

    // Делаем внешнюю обводку потолще
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.8)';
    ctx.lineWidth = 5;
    ctx.stroke();
}

// Функция для получения среднего цвета изображения
function getAverageColor(img) {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = img.width;
    canvas.height = img.height;
    ctx.drawImage(img, 0, 0);
    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height).data;

    let r = 0, g = 0, b = 0;
    for (let i = 0; i < imageData.length; i += 4) {
        r += imageData[i];
        g += imageData[i + 1];
        b += imageData[i + 2];
    }

    const pixels = imageData.length / 4;
    r = Math.round(r / pixels);
    g = Math.round(g / pixels);
    b = Math.round(b / pixels);

    return `rgb(${r},${g},${b})`;
}

// Функция для корректировки цвета
function adjustColor(color, amount) {
    const rgb = color.match(/\d+/g).map(Number);
    return `rgb(${rgb.map(c => Math.max(0, Math.min(255, c + amount))).join(',')})`;
}


/*
=======================================
   Обработчики событий прогресс-бара
=======================================
*/

progressBarContainer.addEventListener('mousemove', (e) => {
    // При движении мыши показываем время, куда перемотается трек
    const rect = progressBarContainer.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const percent = x / rect.width;

    // Если трек уже загружен и известна его длительность, показываем время
    if (audioPlayer.duration) {
        const hoverTime = formatTime(percent * audioPlayer.duration);
        tooltip.textContent = hoverTime;
        tooltip.style.left = `${x}px`;
    }
});

progressBarContainer.addEventListener('mouseenter', () => {
    // Показываем tooltip при наведении
    tooltip.style.display = 'block';
});

progressBarContainer.addEventListener('mouseleave', () => {
    // Скрываем tooltip, когда уводим курсор
    tooltip.style.display = 'none';
});

progressBarContainer.addEventListener('click', function(e) {
    e.preventDefault(); // Предотвращаем стандартное поведение

    console.log('=== Progress Bar Click ===');
    console.log('Player state before click:', {
        paused: audioPlayer.paused,
        currentTime: audioPlayer.currentTime,
        duration: audioPlayer.duration,
        readyState: audioPlayer.readyState
    });

    const rect = this.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const ratio = x / rect.width;
    const targetTime = ratio * audioPlayer.duration;

    console.log('- - Click details:', {
        x: x,
        width: rect.width,
        ratio: ratio,
        targetTime: targetTime
    });

    if (!isNaN(audioPlayer.duration)) {
        const wasPlaying = !audioPlayer.paused;

        if (wasPlaying) {
            console.log('Pausing before seek');
            audioPlayer.pause();
        }

        console.log(`До изменения currentTime: ${audioPlayer.currentTime}`);
        console.log(`Setting currentTime to: ${targetTime}`);
        audioPlayer.currentTime = targetTime;
        console.log(`После изменения currentTime: ${audioPlayer.currentTime}`);

        // Проверим через короткую задержку
        setTimeout(() => {
            console.log(`Через 100мс: currentTime=${audioPlayer.currentTime}`);
        }, 100);

        // Добавляем обработчик для однократного события seeked
        audioPlayer.addEventListener('seeked', function onSeeked() {
            console.log('Seek completed, currentTime:', audioPlayer.currentTime);

            if (wasPlaying) {
                console.log('Resuming playback');
                audioPlayer.play().catch(err => console.error('Play failed:', err));
            }

            audioPlayer.removeEventListener('seeked', onSeeked);
        }, { once: true });
    }
});


/*
=====================================
    Обработчики кнопок управления
=====================================
*/

playPauseBtn.addEventListener('click', () => {
    initAudioContext(); // Инициализируем аудио контекст при первом клике

    if (audioPlayer.paused) {
        audioPlayer.play();
        playPauseBtn.innerHTML = '<i class="fas fa-pause"></i>';
    } else {
        audioPlayer.pause();
        playPauseBtn.innerHTML = '<i class="fas fa-play"></i>';
    }
});

prevBtn.addEventListener('click', () => {
    let wasPaused = audioPlayer.paused;  // Был ли плеер на паузе?
    currentTrackIndex = (currentTrackIndex - 1 + tracks.length) % tracks.length;
    loadTrack(currentTrackIndex);

    if (!wasPaused) {
        audioPlayer.play();
        playPauseBtn.innerHTML = '<i class="fas fa-pause"></i>';
    } else {
        playPauseBtn.innerHTML = '<i class="fas fa-play"></i>';
    }
});

nextBtn.addEventListener('click', () => {
    let wasPaused = audioPlayer.paused;  // Был ли плеер на паузе?
    currentTrackIndex = (currentTrackIndex + 1) % tracks.length;
    loadTrack(currentTrackIndex);

    if (!wasPaused) {
        audioPlayer.play();
        playPauseBtn.innerHTML = '<i class="fas fa-pause"></i>';
    } else {
        playPauseBtn.innerHTML = '<i class="fas fa-play"></i>';
    }
});


/*
================================
   Обработчики событий аудио
================================
*/

// Обновление прогресса
audioPlayer.addEventListener('timeupdate', () => {
    const progress = (audioPlayer.currentTime / audioPlayer.duration) * 100;
    progressBar.style.width = `${progress}%`;
    currentTimeSpan.textContent = formatTime(audioPlayer.currentTime);
});

audioPlayer.addEventListener('loadedmetadata', () => {
    console.log('=== Metadata Loaded ===');
    console.log('Duration:', audioPlayer.duration);
    console.log('Ready State:', audioPlayer.readyState);
    console.log('Current Time:', audioPlayer.currentTime);

    durationSpan.textContent = formatTime(audioPlayer.duration);
});

audioPlayer.addEventListener('seeking', () => {
    console.log('=== Seeking Event ===');
    console.log('Seeking to:', audioPlayer.currentTime);
    console.log('Ready State:', audioPlayer.readyState);
    console.log('Paused:', audioPlayer.paused);
});

audioPlayer.addEventListener('seeked', () => {
    console.log('=== Seeked Event ===');
    console.log('Seeked to:', audioPlayer.currentTime);
    console.log('Ready State:', audioPlayer.readyState);
    console.log('Paused:', audioPlayer.paused);
});

audioPlayer.addEventListener('ended', () => {
    console.log("Событие ended");
    currentTrackIndex = (currentTrackIndex + 1) % tracks.length;
    loadTrack(currentTrackIndex);
    audioPlayer.play();
    playPauseBtn.innerHTML = '<i class="fas fa-pause"></i>'; // Пока не протестил прогресс-бар, не знаю, нужна ли это строчка
});

audioPlayer.addEventListener('error', (e) => {
    console.error('=== Audio Error ===');
    console.error('Error code:', audioPlayer.error.code);
    console.error('Error message:', audioPlayer.error.message);
});

/*
======================================
   Обработчики событий кнопок мышки
======================================
*/

// Зажатие ЛКМ
document.querySelector('.album-cover').addEventListener('mousedown', (e) => {
    isMouseDownOnCover = true;

    initialY = e.clientY;
    initialVolume = audioPlayer.volume;
});

// Движение (при зажатой ЛКМ)
window.addEventListener('mousemove', (e) => {
    if (isMouseDownOnCover) {
        const deltaY = initialY - e.clientY;
        let newVolume = initialVolume + deltaY / 200;
        newVolume = Math.max(0, Math.min(1, newVolume));

        audioPlayer.volume = newVolume;
        updateVolumeVisual(newVolume);
    }
});

// Отпускание зажатой ЛКМ
window.addEventListener('mouseup', () => {
    if (isMouseDownOnCover) {
        isMouseDownOnCover = false;
        initialY = null;
        initialVolume = null;

        // Принудительно скрываем индикатор
        const indicator = document.querySelector('.volume-indicator');
        if (indicator) {
            indicator.style.display = 'none';
        }

        // Обновляем визуальное отображение текущей громкости
        updateVolumeVisual(audioPlayer.volume);
    }
});


/*
================================
         Инициализация
================================
*/

// Функция инициализации аудио-контекста
function initAudioContext() {
    if (!audioContext) {
        audioContext = new (window.AudioContext || window.webkitAudioContext)();
        analyser = audioContext.createAnalyser();
        analyser.fftSize = 256;

        bufferLength = analyser.frequencyBinCount;
        dataArray = new Uint8Array(bufferLength);

        source = audioContext.createMediaElementSource(audioPlayer);
        source.connect(analyser);
        analyser.connect(audioContext.destination);
    }

    // Запускаем визуализацию
    updateVisualizer();
}

// Устанавливаем размеры canvas для визуализации
canvas.width = document.querySelector('.album-cover').offsetWidth;
canvas.height = document.querySelector('.album-cover').offsetHeight;

// Загружаем первый трек при запуске
loadTrack(currentTrackIndex);