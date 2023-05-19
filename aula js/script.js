function alertar(){
	alert("você me clicou");
}

function mensagem(){
	var p = document.getElementsByTagName('p');

	p[0].innerHTML = "Estamos evoluindo";
}
function limpar(){
	var p = document.getElementsByTagName('p');
    p[0].innerHTML = "";
}