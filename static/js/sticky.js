window.onload = function() {
	document.getElementById('circle').onclick = function() {
	var x = setInterval(smooth_scroll, 100);
	}
	function smooth_scroll() {
		document.documentElement.scrollTop = document.documentElement.scrollTop + 100;
		if (document.documentElement.scrollTop >= 600) clearInterval(x);
	}
}
/*window.onscroll = function {scroll()};
var header = document.getElementById('menu');
var stick = header.offsetTop;

function scroll() {
	if (window.pageYOffset >= stick) {
		header.classList.add('sticky');
	} else {
		header.classList.remove('sticky');
	}
}*/