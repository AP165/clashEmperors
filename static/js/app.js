
let inp = document.querySelector('#check');
let inplevel = document.querySelector('#check');


inplevel.addEventListener('click', function() {

let nav = document.querySelector('.navbar-expand-lg');
let body = document.querySelector('body');
let light = document.querySelector('#light');
let tr = document.querySelectorAll('td,th');

    if (inp.checked == true) {
        nav.classList.add('navbar-dark', 'bg-dark');
        nav.classList.remove('navbar-light', 'bg-light');
        light.innerHTML = `
        <span style="color:white">Dark Mode</span>
        `;
        body.classList.add('darkBg');
        for (let i = 0; i < tr.length; i++) {
            tr[i].classList.add('trdark');
            tr[i].classList.remove('trlight');
        }
    }
    if (inp.checked == false) {
        nav.classList.remove('navbar-dark', 'bg-dark');
        nav.classList.add('navbar-light', 'bg-light');
        light.innerHTML = `
        <span style="color:black">light Mode</span>
        `;
        body.classList.remove('darkBg');
        for (let i = 0; i < tr.length; i++) {
            tr[i].classList.remove('trdark');
            tr[i].classList.add('trlight');
        }
    }
});