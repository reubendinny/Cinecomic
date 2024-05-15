// let images = document.querySelectorAll('.carousel img');
// let currentImage = 0;

// setInterval(() => {
//     images[currentImage].classList.remove('active');
//     currentImage = (currentImage + 1) % images.length;
//     images[currentImage].classList.add('active');
// }, 5000);

// let box = document.querySelector('.box');

// setTimeout(() => {
//     box.classList.add('visible');
// }, 2000);


//----------------
//new start===========
const carousel = document.querySelector('.carousel');
const images = carousel.children;
let currentImage = 0;

setInterval(() => {
    currentImage = (currentImage + 1) % images.length;
    carousel.style.transform = `translateX(-${currentImage * 100}%)`;
}, 5000);

const box = document.querySelector('.box');

setTimeout(() => {
    box.classList.add('visible');
}, 2000);
//============new end

