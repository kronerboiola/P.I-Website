var i = 0;

function get_msg(new_msg) {
	msg = new_msg;
}

function typewrite() {
	if (i<msg.length) {
		document.getElementsByTagName('h1')[0].innerHTML += msg[i];
		i++;
		setTimeout(typewrite, 125); //not working...
	}
}