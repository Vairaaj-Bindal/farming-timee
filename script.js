// Add smooth background animation
const background = document.querySelector('.background');

function animateBackground() {
    let hue = 120; // Initial hue value (green)
    setInterval(() => {
        hue = (hue + 1) % 360;
        const gradient = `linear-gradient(to bottom, hsl(${hue}, 100%, 50%), hsl(${(hue + 60) % 360}, 100%, 50%))`;
        background.style.background = gradient;
    }, 50); // Adjust the interval for smoother or faster animation
}

animateBackground();
