// Надпись RUB на верхней планке
const rubEl = document.querySelector('.alert1');
rubEl.addEventListener('click', function(e) {
    alert('Куда ты свои рученки тянешь\nк иностранной валюте?\nТолько наш' +
        ' деревянный!!!\nТолько хардкор!!!');
});

// Надпись Помощь разработчику на верхней планке
const helpDev = document.querySelector('.help_dev');
helpDev.addEventListener('click', function(e) {
    alert('ОЙ Спасибо!!!\nОЙ на доширак.\nОЙ по номеру телефона через СБП :)');
});

// Надпись про адрес получения на верхней планке
const addressEL = document.querySelector('.address');
addressEL.addEventListener('click', function(e) {
    alert('Либо самовывоз из Китая.');
});