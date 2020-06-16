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

let predictionButton = document.querySelector("#prediction-button")
let valueToPredict = document.querySelector("#prediction-input")
let illnessSelected = document.querySelector("#illness-select")
let resultTextArea = document.querySelector("#prediction-result")
let resultDiv = document.querySelector("#result")

    
predictionButton.addEventListener("click", async () => {
    if (illnessSelected.value !== "") {
        resultDiv.className = "animate__animated animate__fadeInLeft";
        resultDiv.setAttribute("style", "display: block");

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
                resultTextArea.textContent = data.prediction
                return data.prediction
            }
        )
    } else {
        alert("Selecciona una condición de salud")
    }
})

illnessSelected.addEventListener("change", () => {
    console.log("change image...")
    // set image to selected medical condition
    let imageArea = document.querySelector("#img-container")
    imageArea.style.backgroundImage = `url(/static/images/plot_${illnessSelected.value}.png)`
})

let getResults = document.querySelector("#illness-button")
getResults.addEventListener("click", () => {
    console.log("change image...")
    // set image to selected medical condition
    let imageArea = document.querySelector("#img-container")
    imageArea.style.backgroundImage = `url(/static/images/plot_${illnessSelected.value}.png)`
})

