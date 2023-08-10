const wrapper = document.querySelector(".wrapper");
const loginLink = document.querySelector(".login-link");
const registerLink = document.querySelector(".register-link");
const btnPopup = document.querySelector(".btnLogin-popup");
const btnPopupClose = document.querySelector(".close-icon");


registerLink.addEventListener("click", () => {
    wrapper.classList.add("online");
});

loginLink.addEventListener("click", () => {
    wrapper.classList.remove("online");
});

btnPopup.addEventListener("click", () => {
    wrapper.classList.add("online-popup");
    wrapper.classList.remove("online");
});

btnPopupClose.addEventListener("click", () => {
    wrapper.classList.remove("online-popup");
});