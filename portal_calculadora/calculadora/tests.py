from django.test import TestCase
from .utils import Calculadora

class CalculadoraTestCase(TestCase):
    """
    Testes unitários para a classe Calculadora.
    Verifica operações básicas e tratamentos de erro.
    """
        
    def test_soma(self):
        calc = Calculadora(10, 5, '+')
        self.assertEqual(calc.calcular(), 15)

    def test_subtracao(self):
        calc = Calculadora(10, 5, '-')
        self.assertEqual(calc.calcular(), 5)

    def test_divisao_zero(self):
        calc = Calculadora(10, 0, '/')
        self.assertEqual(calc.calcular(), 'Erro: divisão por 0')

    def test_operador_invalido(self):
        calc = Calculadora(10, 5, '^')
        self.assertEqual(calc.calcular(), 'Erro: Operador inválido')
