class Calculadora:
    def __init__(self, primeiro_numero, segundo_numero=None, operador=None):
        self.primeiro_numero = float(primeiro_numero)
        self.segundo_numero = float(segundo_numero) if segundo_numero is not None else 0.0
        self.operador = operador

    def calcular(self):
        if self.operador in self.operacoes_binarias():
            return self.operacoes_binarias()[self.operador](self.primeiro_numero, self.segundo_numero)
        else:
            return 'Erro: Operador inválido'

    @staticmethod
    def operacoes_binarias():
        return {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b if b != 0 else 'Erro: Divisão por zero',
            '%': lambda a, b: (a / 100) * b,
        }
    