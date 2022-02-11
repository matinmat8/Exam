function focus (elm, use) {
    use? elm.parentNode.querySelector(".placeholder").classList.add("active"):
        this.parentNode.querySelector(".placeholder").classList.add("active");
}

function blur () {    
    if (this.value || (this.type == "number" && !+this.value))
        return null;

    this.parentNode.querySelector(".placeholder").classList.remove("active");
}

document.querySelectorAll(".input input, .date input").forEach(
    input => {
        input.addEventListener("focus", focus);
        input.addEventListener("blur", blur);

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