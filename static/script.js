const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login');
const RegisterLink = document.querySelector('.registro');
const BtnLogin = document.querySelector('.btnLogin');
const BtnFechar = document.querySelector('.icone-fechar')

RegisterLink.addEventListener('click', ()=>{
    wrapper.classList.add('active');
});

loginLink.addEventListener('click', ()=>{
    wrapper.classList.remove('active');
});

BtnLogin.addEventListener('click', ()=>{
    wrapper.classList.add('popup-ativo');
})

BtnFechar.addEventListener('click', ()=>{
    wrapper.classList.remove('popup-ativo');
})