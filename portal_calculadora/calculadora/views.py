from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Operacao
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

class CustomLoginView(LoginView):
    template_name = 'calculadora/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

@login_required
def index(request):
    historico = Operacao.objects.filter(usuario=request.user).order_by('-data_inclusao')[:10]

    if request.method == 'POST':
        numero1 = request.POST.get('num1')
        numero2 = request.POST.get('num2')
        operador = request.POST.get('operador')
        
        try:
            n1 = float(numero1)
            n2 = float(numero2)

            if operador == '+':
                resultado = n1 + n2
            elif operador == '-':
                resultado = n1 - n2
            elif operador == '*':
                resultado = n1 * n2
            elif operador == '/':
                resultado = n1 / n2 if n2 != 0 else 'Erro'
            else:
                resultado = 'Inválido'

            # Salvando operação
            Operacao.objects.create(
                usuario=request.user,
                parametros=f'{n1} {operador} {n2}',
                tipo=operador,
                resultado=str(resultado)
            )

            return redirect('/')
        except:
            resultado = 'Erro'
    
    return render(request, 'calculadora/index.html', {'historico': historico})

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

            # Login automático após cadastro
            login(request, user)

            return redirect('index')

    return render(request, 'calculadora/register.html')

