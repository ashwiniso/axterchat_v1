// Selecting DOM elements using class names and assigning them to variables
const wrapper = document.querySelector(".wrapper");              // The main wrapper element
const loginLink = document.querySelector(".login-link");         // The login link element
const registerLink = document.querySelector(".register-link");   // The register link element
const btnPopup = document.querySelector(".btnLogin-popup");      // The popup button element
const btnPopupClose = document.querySelector(".close-icon");     // The close button element

// Adding a click event listener to the "registerLink" element
registerLink.addEventListener("click", () => {
    // When the "registerLink" is clicked, add the "online" class to the "wrapper" element
    wrapper.classList.add("online");
});

// Adding a click event listener to the "loginLink" element
loginLink.addEventListener("click", () => {
    // When the "loginLink" is clicked, remove the "online" class from the "wrapper" element
    wrapper.classList.remove("online");
});

// Adding a click event listener to the "btnPopup" element
btnPopup.addEventListener("click", () => {
    // When the "btnPopup" is clicked, add the "online-popup" class and remove the "online" class from the "wrapper" element
    wrapper.classList.add("online-popup");
    wrapper.classList.remove("online");
});

// Adding a click event listener to the "btnPopupClose" element
btnPopupClose.addEventListener("click", () => {
    // When the "btnPopupClose" is clicked, remove the "online-popup" class from the "wrapper" element
    wrapper.classList.remove("online-popup");
});
