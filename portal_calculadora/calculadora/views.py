from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Operacao
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .utils import Calculadora

@login_required
def index(request):
    """
    View principal da calculadora.
    - Exibe a interface principal
    - Processa os cálculos 
    - Salva operações no banco
    - Permite limpar histórico
    """
    # Recupera as últimas operações do usuário logado
    historico = Operacao.objects.filter(usuario=request.user).order_by('-data_inclusao')
    resultado = ''  # Garantimos que a variável exista, mesmo no GET

    if request.method == 'POST':
        action = request.POST.get('action')

        # Caso o usuário clique em "Limpar Histórico"
        if action == 'clear_history':
            Operacao.objects.filter(usuario=request.user).delete()
            return redirect('index')

        # Dados recebidos do JavaScript pelo form oculto
        primeiro_numero = request.POST.get('num1')
        segundo_numero = request.POST.get('num2')
        operador = request.POST.get('operador')

        # Cria instância da calculadora e executa o cálculo
        calc = Calculadora(primeiro_numero, segundo_numero, operador)
        resultado = calc.calcular()

        # Salva a operação no banco de dados
        Operacao.objects.create(
            usuario=request.user,
            parametros=f"{primeiro_numero}{operador}{segundo_numero}",
            resultado=resultado
        )

        # Atualiza histórico após novo cálculo
        historico = Operacao.objects.filter(usuario=request.user).order_by('-data_inclusao')

    return render(request, 'calculadora/index.html', {
        'historico': historico,
        'display_result': resultado
    })
