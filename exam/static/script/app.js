const openMenuBtn = document.querySelector(".links .open"),
    prevent = document.getElementById("prevent"),
    menu = document.querySelector("aside.menu");


function openMenu () {
    menu.style.left = "0";
    prevent.style.zIndex = "0";
}

function closeMenu () {
    menu.style.left = "-180px";
    prevent.style.zIndex = "-1";
}

openMenuBtn.addEventListener("click", openMenu);
prevent.addEventListener("click", closeMenu);