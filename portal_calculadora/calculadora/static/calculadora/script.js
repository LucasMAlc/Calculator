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

    // Operações unárias
    if (op === 'inv') {
        document.getElementById('num1').value = current;
        document.getElementById('operador').value = 'inv';
        document.getElementById('calc-form').submit();
        return;
    }

    // Operações binárias normais
    operador = op;
    primeiro_numero = current;
    current += op;
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
    let match = current.match(/^(-?\d+\.?\d*)([+\-*/%])(-?\d+\.?\d*)$/);
    if (!match) return;

    primeiro_numero = match[1];
    operador = match[2];
    segundo_numero = match[3];

    document.getElementById('num1').value = primeiro_numero;
    document.getElementById('num2').value = segundo_numero;
    document.getElementById('operador').value = operador;

    document.getElementById('calc-form').submit();
}
