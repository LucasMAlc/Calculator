from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Operacao(models.Model):
    TIPO_OPERACAO = [
        ('+', 'Soma'),
        ('-', 'Subtração'),
        ('*', 'Multiplicação'),
        ('/', 'Divisão'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    parametros = models.CharField(max_length=255)
    tipo = models.CharField(max_length=1, choices=TIPO_OPERACAO)
    resultado = models.CharField(max_length=255)
    data_inclusao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.parametros} {self.tipo} = {self.resultado}"
