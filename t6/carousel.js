var carouselItems = document.querySelectorAll('.carousel-item');
var currentIndex = 0;
var intervalId;

function showNextItem() {
    carouselItems[currentIndex].classList.remove('active');
    currentIndex = (currentIndex + 1) % carouselItems.length;
    carouselItems[currentIndex].classList.add('active');
}

function startCarousel() {
    intervalId = setInterval(showNextItem, 2000); 
}

function stopCarousel() {
    clearInterval(intervalId);
}

window.onload = function () {
    startCarousel();

    for (var i = 0; i < carouselItems.length; i++) {
        var image = carouselItems[i].querySelector('.slideImg');
        
        image.setAttribute('data-mouseover', 'false');

        image.addEventListener('mouseover', function () {
            this.setAttribute('data-mouseover', 'true');
            stopCarousel();
        });

        image.addEventListener('mouseout', function () {
            this.setAttribute('data-mouseover', 'false');
            startCarousel();
        });
    }
};
function openPopup() {
    document.getElementById('popup').style.display = 'block';
}

function closePopup() {
    document.getElementById('popup').style.display = 'none';
}