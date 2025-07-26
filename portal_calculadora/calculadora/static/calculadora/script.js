let current = '';
let operador = '';
let num1 = '';
let num2 = '';

function updateDisplay(value) {
    document.getElementById('display').value = value;
}

function append(char) {
    current += char;
    updateDisplay(current);
}

function setOperator(op) {
    if (!current) return;
    operador = op;
    num1 = current;
    current += op; // ex: "2+"
    updateDisplay(current);
}

function clearDisplay() {
    current = '';
    operador = '';
    num1 = '';
    num2 = '';
    updateDisplay('');
}

function invertSign() {
    // aplica ao último número digitado
    let lastNumber = current.match(/(-?\d+\.?\d*)$/);
    if (lastNumber) {
        let original = lastNumber[0];
        let inverted = parseFloat(original) * -1;
        current = current.replace(/(-?\d+\.?\d*)$/, inverted);
        updateDisplay(current);
    }
}

function calculate() {
    // Extrai número antes e depois do operador
    let match = current.match(/^(-?\d+\.?\d*)([+\-*/%])(-?\d+\.?\d*)$/);
    if (!match) return;

    num1 = match[1];
    operador = match[2];
    num2 = match[3];

    document.getElementById('num1').value = num1;
    document.getElementById('num2').value = num2;
    document.getElementById('operador').value = operador;

    document.getElementById('calc-form').submit();
}
