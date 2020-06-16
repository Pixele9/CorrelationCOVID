var checkbox = document.querySelector('input[name=theme]');

theme = localStorage.getItem('theme');
if (theme != null && theme != undefined){
    document.documentElement.setAttribute('data-theme', theme);
    if (theme == 'dark') {
        checkbox.checked = true;
    } else {
        checkbox.checked = false;
    }
}

checkbox.addEventListener('change', function() {
    if(this.checked) {
        trans()
        localStorage.setItem('theme', "dark");
        document.documentElement.setAttribute('data-theme', 'dark')
    } else {
        trans()
        localStorage.setItem('theme', "light");
        document.documentElement.setAttribute('data-theme', 'light')
    }
})

let trans = () => {
    document.documentElement.classList.add('transition');
    window.setTimeout(() => {
        document.documentElement.classList.remove('transition')
    }, 1000)
}

let resultDiv = document.querySelector("#result")
let predictionButton = document.querySelector("#prediction-button")
let valueToPredict = document.querySelector("#prediction-input")
let illnessSelected = document.querySelector("#illness-select").value
predictionButton.addEventListener("click", () => {
    resultDiv.className = "animate__animated animate__fadeInRight";
    resultDiv.setAttribute("style", "display: block");
    let options = {
        method: "POST",
        headers: {'Content-Type':'application/json'},
        body: valueToPredict.value
    }
    fetch(`predict/${illnessSelected}`, options)
})