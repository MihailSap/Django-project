function openFullscreen(imageElement) {
    const overlay = document.getElementById('fullscreenOverlay');
    const fullscreenImage = document.getElementById('fullscreenImage');
    fullscreenImage.src = imageElement.src;
    overlay.style.display = 'flex';
}

function closeFullscreen() {
    const overlay = document.getElementById('fullscreenOverlay');
    overlay.style.display = 'none';
}