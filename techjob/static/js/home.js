document.addEventListener('DOMContentLoaded', function () {
    const carouselItems = document.querySelectorAll('.carousel-item');
    let currentIndex = 0;

    // Mostrar o primeiro item do carrossel
    carouselItems[currentIndex].classList.add('active');

    function showNext() {
        carouselItems[currentIndex].classList.remove('active');
        currentIndex = (currentIndex + 1) % carouselItems.length;
        carouselItems[currentIndex].classList.add('active');
    }

    setInterval(showNext, 3000); // Muda a imagem a cada 3 segundos
});
