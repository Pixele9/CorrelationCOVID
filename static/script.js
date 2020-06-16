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

let predictionButton = document.querySelector("#prediction-button")
let valueToPredict = document.querySelector("#prediction-input")
let illnessSelected = document.querySelector("#illness-select")
let resultTextArea = document.querySelector("#prediction-result")

predictionButton.addEventListener("click", async () => {
    let options = {
        method: "POST",
        headers: {'Content-Type':'application/json'},
        body: valueToPredict.value
    }

    await fetch(`predict/${illnessSelected.value}`, options)
    .then(
        response => response.json()
    )
    .then(
        data => {
            console.log("Prediciton: ", data.prediction)
            return data.prediction
        }
    )
})

let getResults = document.querySelector("#illness-button")
getResults.addEventListener("click", () => {
    console.log("change image...")
    let imageArea = document.querySelector("#img-container")
    // set image to selected medical condition
    imageArea.style.backgroundImage = `url(/static/images/plot_${illnessSelected.value}.png)`
})

