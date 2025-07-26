let current = '';
let operador = '';
let num1 = '';
let num2 = '';

function append(char) {
    current += char;
    document.getElementById('display').value = current;
}

function setOperator(op) {
    if (!current) return;
    operador = op;
    num1 = current;
    current = '';
    document.getElementById('display').value = '';
}

function clearDisplay() {
    current = '';
    operador = '';
    num1 = '';
    num2 = '';
    document.getElementById('display').value = '';
}

function invertSign() {
    if (current) {
        current = String(parseFloat(current) * -1);
        document.getElementById('display').value = current;
    }
}

function calculate() {
    if (!operador || !current) return;
    num2 = current;

    document.getElementById('num1').value = num1;
    document.getElementById('num2').value = num2;
    document.getElementById('operador').value = operador;

    document.getElementById('calc-form').submit();
}
