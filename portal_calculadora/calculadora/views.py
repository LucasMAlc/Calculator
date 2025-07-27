from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Operacao
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .utils import Calculadora


class CustomLoginView(LoginView):
    template_name = 'calculadora/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

@login_required
def index(request):
    historico = Operacao.objects.filter(usuario=request.user).order_by('-data_inclusao')[:10]
    resultado = ''  # ← valor padrão vazio para evitar erro

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'clear_history':
            Operacao.objects.filter(usuario=request.user).delete()
            return redirect('index')

        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        operador = request.POST.get('operador')

        calc = Calculadora(num1, num2, operador)
        resultado = calc.calcular()

        Operacao.objects.create(
            usuario=request.user,
            parametros=f"{num1}{operador}{num2}",
            resultado=resultado
        )

        historico = Operacao.objects.filter(usuario=request.user).order_by('-data_inclusao')[:10]

    return render(request, 'calculadora/index.html', {
        'historico': historico,
        'display_result': resultado
    })


def register(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já existe.')
        else:
            user = User.objects.create_user(username=nome, email=email, password=senha)
            user.save()

            login(request, user)  # login automático
            return redirect('index')

    return render(request, 'calculadora/register.html')

