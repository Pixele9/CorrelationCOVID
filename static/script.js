var checkbox = document.querySelector('input[name=theme]');

checkbox.addEventListener('change', function() {
    if(this.checked) {
        trans()
        document.documentElement.setAttribute('data-theme', 'dark')
    } else {
        trans()
        document.documentElement.setAttribute('data-theme', 'light')
    }
})

let trans = () => {
    document.documentElement.classList.add('transition');
    window.setTimeout(() => {
        document.documentElement.classList.remove('transition')
    }, 1000)
}


let predictionButton = document.querySelector("#pedict-button")
let valueToPredict = document.querySelector("#prediction-input")
let illnessSelected = document.querySelector("#illness-select").value
predictionButton.addEventListener("click", () => {
    let options = {
        method: "POST",
        headers: {'Content-Type':'application/json'},
        body: valueToPredict.value
    }
    fetch(`predict/${illnessSelected}`, options)
})