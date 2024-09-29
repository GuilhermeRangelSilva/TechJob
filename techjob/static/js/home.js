function showNextImage() {
    items[currentIndex].style.opacity = 0; // Oculta a imagem atual
    currentIndex = (currentIndex + 1) % totalItems; // Avança para a próxima imagem
    items[currentIndex].style.opacity = 1; // Mostra a nova imagem
}

setInterval(showNextImage, 3000); // Muda a imagem a cada 3 segundos