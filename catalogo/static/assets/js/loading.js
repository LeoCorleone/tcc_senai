document.addEventListener("DOMContentLoaded", function () {
    showLoadingOverlay(); 

    setTimeout(function () {
        hideLoadingOverlay(); 
    }, 1000);
});

function showLoadingOverlay() {
    var loadingOverlay = document.getElementById("loadingOverlay");
    if (loadingOverlay) {
        loadingOverlay.style.display = "flex"; 
    }
}

function hideLoadingOverlay() {
    var loadingOverlay = document.getElementById("loadingOverlay");
    if (loadingOverlay) {
        loadingOverlay.style.display = "none"; 
    }
}
