from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

def register(request):
    """
    View responsável pelo registro de novos usuários.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # login automático após cadastro
            return redirect('index')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})
