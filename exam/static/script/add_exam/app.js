function focus () {
    this.parentNode.querySelector(".placeholder").classList.add("active");
}

function blur () {    
    if (this.value)
        return null;

    this.parentNode.querySelector(".placeholder").classList.remove("active");
}

document.querySelectorAll(".input input, .date input").forEach(
    input => {
        input.addEventListener("focus", focus);
        input.addEventListener("blur", blur);
    }
);

function focusToInput () {
    this.previousElementSibling.focus();
}

document.querySelectorAll(".placeholder").forEach(
    placeholder => placeholder.addEventListener("click", focusToInput)
);