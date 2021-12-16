var S=document.styleSheets;

document.getElementById('delete').onclick = function () {
    S[0].disabled = true;
}

document.getElementById('set').onclick = function () {
    S[0].disabled = false;
}