window.onscroll = function() {slide_menu()};

function slide_menu() {
	menu = document.getElementById('menu');
	if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
		menu.style.top = '-16px';
	} else {
		menu.style.top = '-670px';
	}
}