console.log("teste")
var titulo = document.querySelector("h1")

console.log(titulo.textContent)
titulo.textContent = "teste novo"

function mostrarAlerta(){
    alert("Funciona!");
}

function createButton(){
    var btn = document.createElement('BUTTON');
    var lbl = document.createTextNode('CLICK ME');
    btn.appendChild(lbl);
    btn.onclick = function() {
        console.log(titulo.textContent);
    }
    document.body.appendChild(btn);
}

createButton();

mostrarAlerta()

var botao = document.querySelector("#botaoEnviar")
botao.onclick = mostrarAlerta;