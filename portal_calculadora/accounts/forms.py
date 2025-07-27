from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomUserCreationForm(forms.ModelForm):
    """
    Formulário personalizado de criação de usuário.
    Utiliza os campos: nome de usuário, email e senha.
    """
    senha = forms.CharField(widget=forms.PasswordInput, label='Senha')
    confirmar_senha = forms.CharField(widget=forms.PasswordInput, label='Confirmar Senha')

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        """
        Validação para garantir que senha e confirmação sejam iguais.
        """
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        if senha and confirmar_senha and senha != confirmar_senha:
            raise ValidationError("As senhas não coincidem.")

        return cleaned_data

    def save(self, commit=True):
        """
        Sobrescreve o método save para definir a senha corretamente.
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["senha"])
        if commit:
            user.save()
        return user
