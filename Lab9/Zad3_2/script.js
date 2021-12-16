class MyCounter extends HTMLElement {
    constructor() {
        super();
        this.shadow = this.attachShadow({ mode: "open"});
    }

    static get observedAttributes() {
        return ["value"]
    }

    get value() {
        return this.getAttribute('value')
    }

    set value(val) {
        this.setAttribute('value', val)
    }

    
    attributeChangedCallback(change) {
        if (change === 'value') this.render();
    }

    connectedCallback() {
        this.render();
    }

    render() {
        this.shadow.innerHTML = `
        <span>${this.value === null ? 0 : this.value - 1}</span>
        `
    }

}

customElements.define('my-counter', MyCounter);

function updateSpan(){
    current = document.getElementById("licznik").valueAsNumber;
    if (current > 0) {
        spans = document.getElementsByTagName("my-counter");
        for (let i = 0; i < 10; i++) {
            spans[i].setAttribute('value', current)
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
