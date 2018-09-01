function email_validator() {
	var email = form1.email.value;
	if (!(email.endsWith('.com') || email.endsWith('.net'))) {
		alert('E-mail inválido!');
	}
}