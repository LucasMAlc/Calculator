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
    if request.method == 'POST':
        # Checar se foi o botão "limpar histórico"
        if request.POST.get('action') == 'clear_history':
            Operacao.objects.filter(usuario=request.user).delete()
            return redirect('/')

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
            elif operador == '%':
                resultado = (n1 / 100) * n2
            else:
                resultado = 'Inválido'

            # Registrar operação
            Operacao.objects.create(
                usuario=request.user,
                parametros=f'{n1} {operador} {n2}',
                tipo=operador,
                resultado=str(resultado)
            )

            return redirect('/')
        except:
            pass  # Se der erro, só recarrega sem registrar

    historico = Operacao.objects.filter(usuario=request.user).order_by('-data_inclusao')

    context = {
        'historico': historico,
        'display_result': '',
    }

    if request.method == 'POST' and 'resultado' in locals():
        context['display_result'] = resultado  # isso será passado pro display após clicar "="

    return render(request, 'calculadora/index.html', context)



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

