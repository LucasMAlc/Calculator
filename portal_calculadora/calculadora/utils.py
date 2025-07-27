class Calculadora:
    """
    Classe responsável por executar operações matemáticas básicas
    com base em dois números e um operador recebido.
    """

    def __init__(self, primeiro_numero, segundo_numero=None, operador=None):
        """
        Inicializa a calculadora com os valores fornecidos.
        """
        self.primeiro_numero = float(primeiro_numero)
        self.segundo_numero = float(segundo_numero) if segundo_numero is not None else 0.0
        self.operador = operador

    def calcular(self):
        """
        Executa o cálculo baseado no operador e retorna o resultado.
        Se operador for inválido, retorna mensagem de erro.
        """
        if self.operador in self.operacoes_binarias():
            return self.operacoes_binarias()[self.operador](
                self.primeiro_numero, self.segundo_numero
            )
        return 'Erro: Operador inválido'

    @staticmethod
    def operacoes_binarias():
        """
        Dicionário que mapeia cada operador a uma função lambda correspondente.
        """
        return {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b if b != 0 else 'Erro: divisão por 0',
            '%': lambda a, b: (a / 100) * b,
        }
