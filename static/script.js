var checkbox = document.querySelector('input[name=theme]');

checkbox.addEventListener('change', function() {
<<<<<<< HEAD
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
=======
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
>>>>>>> 6df71989d0d697ae9c8187b465011487f3d6c742
}