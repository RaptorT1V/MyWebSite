const text = "Welcome to Genius Web Site";
const container = document.getElementById("gravity-text");
const letters = text.split("");

let initialPositions = [];

letters.forEach((letter, index) => {
    const span = document.createElement("span");
    span.textContent = letter;
    container.appendChild(span);

    const angle = Math.random() * Math.PI * 2;
    const radius = Math.random() * 400 + 200;
    const x = Math.cos(angle) * radius;
    const y = Math.sin(angle) * radius;

    span.style.left = `${x}px`;
    span.style.top = `${y}px`;

    initialPositions.push({ x: x, y: y });

    setTimeout(() => {
        span.classList.add("active");
        span.style.left = `${index * 15 - (letters.length * 15) / 2}px`;
        span.style.top = '0px';
        span.style.animation = 'pulse 2s infinite';
    }, 50 * index);
});

container.addEventListener("mousemove", (e) => {
    const spans = container.querySelectorAll("span");
    spans.forEach((span, index) => {
        const rect = span.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;

        const dx = e.clientX - centerX;
        const dy = e.clientY - centerY;

        const distance = Math.sqrt(dx * dx + dy * dy);
        const force = Math.min(100, 2000 / (distance + 1));

        const angle = Math.atan2(dy, dx);
        const moveX = Math.cos(angle) * force;
        const moveY = Math.sin(angle) * force;

        span.style.transform = `translate(${moveX}px, ${moveY}px)`;
    });
});

container.addEventListener("click", () => {
    const spans = container.querySelectorAll("span");
    spans.forEach((span, index) => {
        span.style.transition = 'all 0.5s ease';
        span.style.left = `${initialPositions[index].x}px`;
        span.style.top = `${initialPositions[index].y}px`;
        span.style.transform = 'translate(0, 0)';
        span.style.opacity = 0;

        setTimeout(() => {
            span.style.transition = 'all 0.5s ease';
            span.style.left = `${index * 17 - (letters.length * 17) / 2}px`;
            span.style.top = '0px';
            span.style.opacity = 1;
        }, 1000);
    });
});