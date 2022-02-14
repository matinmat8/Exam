const passwordInputs = document.querySelectorAll("input[type=password]");

function showPassword () {
    passwordInputs.forEach(
        input => input.type == "password"? input.type = "text": input.type = "password"
    );
}

document.querySelector(".show-password input").addEventListener("change", showPassword);