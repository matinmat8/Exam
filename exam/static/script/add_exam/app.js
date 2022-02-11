function focus (elm, use) {
    use? elm.parentNode.querySelector(".placeholder").classList.add("active"):
        this.parentNode.querySelector(".placeholder").classList.add("active");
}

document.querySelectorAll(".input input, .date input").forEach(
    input => {
        input.addEventListener("focus", focus);

        if (input.value)
            focus(input, true)
    }
);

function focusToInput () {
    this.previousElementSibling.focus();
}

document.querySelectorAll(".placeholder").forEach(
    placeholder => placeholder.addEventListener("click", focusToInput)
);