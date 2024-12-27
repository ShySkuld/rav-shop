
// Помощь разработчику
const pop_up = document.querySelector('.helpDevWindow');
const openPopup = document.querySelector('.helpDev');
const closePopup = document.querySelector('.closePopup');

openPopup.addEventListener('click', function(e) {
    pop_up.style.display = 'flex';
});

closePopup.addEventListener('click', function(e) {
    pop_up.style.display = 'none';
});

// Надпись RUB на верхней планке
const rubEl = document.querySelector('.rub_change');
rubEl.addEventListener('click', function(e) {
    alert('\n\nКуда ты свои рученки тянешь\nк иностранной валюте?\nТолько наш' +
        ' деревянный!!!\nТолько хардкор!!!');
});

// Надпись про адрес получения на верхней планке
const addressEL = document.querySelector('.address');
addressEL.addEventListener('click', function(e) {
    alert('\n\nЛибо самовывоз из Китая.');
});