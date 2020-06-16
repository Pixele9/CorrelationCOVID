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
let resultDiv = document.querySelector("#result-container")

    
predictionButton.addEventListener("click", async () => {
    if (illnessSelected.value !== "") {
        resultDiv.className = "animate__animated animate__fadeInLeft";
        resultDiv.setAttribute("style", "display: flex");

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

let pearsonText = document.getElementById("pearson-text")
let mediaText = document.getElementById("media-text")
let varianzaText = document.getElementById("varianza-text")
let desviacionText = document.getElementById("desviacion-text")

// Fires on selection change
illnessSelected.addEventListener("change", async () => {
    // set image to selected medical condition
    let imageArea = document.querySelector("#img-container")
    imageArea.style.backgroundImage = `url(/static/images/plot_${illnessSelected.value}.png)`

    let options = {
        method: "GET",
    }

    await fetch(`stats/${illnessSelected.value}`, options)
        .then(
            response => response.json()
        )
        .then(
            data => {
                console.log(data)
                // resultTextArea.textContent = data.prediction
                pearsonText.textContent = data.pearson
                mediaText.textContent = data.mean
                varianzaText.textContent = data.variance
                desviacionText.textContent = data.std_dev
            }
        )
})


// let getResults = document.querySelector("#illness-button")
// getResults.addEventListener("click", () => {
//     console.log("change image...")
//     // set image to selected medical condition
//     let imageArea = document.querySelector("#img-container")
//     imageArea.style.backgroundImage = `url(/static/images/plot_${illnessSelected.value}.png)`
// })

let creditButton = document.querySelector("#credits-button")
creditButton.addEventListener("click", () => {
    Swal.fire({
        title: 'Desarrolladores',
        html: 'Andrés Leal Aguilar<br>Raúl Guzmán Guerrero<br>Luis Arturo García Gonzalez',
        imageUrl: 'https://c1.staticflickr.com/3/2654/4087602766_73ed52908d_b.jpg',
        imageWidth: 400,
        imageHeight: 200,
        imageAlt: 'Facultad de informatica - UAQ',
    })
})