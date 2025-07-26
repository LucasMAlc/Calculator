from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Operacao

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
