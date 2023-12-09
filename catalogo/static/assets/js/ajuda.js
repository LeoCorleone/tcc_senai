// Função para exibir a caixa de diálogo de ajuda ao lado do botão
function exibirAjuda() {
    var ajudaDialogo = document.getElementById("ajuda-dialogo");
    var botaoAjuda = document.getElementById("botao-ajuda");

    if (ajudaDialogo && botaoAjuda) {
        var botaoRetangulo = botaoAjuda.getBoundingClientRect();
        ajudaDialogo.style.display = "block";
        ajudaDialogo.style.top = window.scrollY + botaoRetangulo.top + "px";
        ajudaDialogo.style.left = window.scrollX + botaoRetangulo.right + "px";
    }
}

// Função para fechar a caixa de diálogo de ajuda
function fecharAjuda() {
    document.getElementById("ajuda-dialogo").style.display = "none";
}

// Adiciona um ouvinte de eventos ao evento DOMContentLoaded
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("botao-ajuda").addEventListener("click", exibirAjuda);
});
