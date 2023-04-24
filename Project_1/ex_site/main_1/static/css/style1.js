'use strict';

(function () {
    var body = document.body;
    var burgerMenu = document.getElementsByClassName('b-menu')[0];
    var burgerContain = document.getElementsByClassName('b-container')[0];
    var burgerNav = document.getElementsByClassName('b-nav')[0];

    burgerMenu.addEventListener('click', function toggleClasses() {
        [body, burgerContain, burgerNav].forEach(function (el) {
            el.classList.toggle('open');
        });
    }, false);
})();
/* edit_account */
let edit_but = document.querySelector('.edit_account')
let edit = document.querySelector('.edit') /* блок формы редактирования */
edit_but.addEventListener('click', opent_edit_account);

function opent_edit_account() {
    edit.style.display = 'block'
}
let edit_close = document.querySelector('.edit_close')
edit_close.addEventListener('click', close_edit_account)
function close_edit_account() {
    edit.style.display = 'none'
}
let leave_review = document.querySelector('.leave_review')
let form_review_personal = document.querySelector('.main_review_personal')
leave_review.addEventListener('click', open_form_review)

function open_form_review() {
    form_review_personal.style.display = 'flex'
}
let close_reviews = document.querySelector('.review_close')
close_reviews.addEventListener('click', close_form_reviews)

function close_form_reviews() {
    form_review_personal.style.display = 'none'
}