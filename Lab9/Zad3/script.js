function updateSpan(){
    current = document.getElementById("licznik").valueAsNumber;
    if (current > 0) {
        spans = document.getElementsByTagName("span");
        for (let i = 0; i < 10; i++) {
            spans[i].textContent = current - 1;
        }
    }
    if (current <= 0) {
        document.getElementById('licznik').value = 0;
    }
    else {
    document.getElementById('licznik').value = current - 1;
    }
}

setInterval(updateSpan, 1000);