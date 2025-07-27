from django.test import TestCase
from .utils import Calculadora

class CalculadoraTestCase(TestCase):
    def test_soma(self):
        calc = Calculadora(10, 5, '+')
        self.assertEqual(calc.calcular(), 15)

    def test_inversao(self):
        calc = Calculadora(10, None, 'inv')
        self.assertEqual(calc.calcular(), -10)

    def test_divisao_zero(self):
        calc = Calculadora(10, 0, '/')
        self.assertEqual(calc.calcular(), 'Erro: Divisão por zero')

    def test_operador_invalido(self):
        calc = Calculadora(10, 5, '^')
        self.assertEqual(calc.calcular(), 'Erro: Operador inválido')
