from django import forms
from .models import *

class PostagemForms(forms.ModelForm):
    class Meta:
        model = Roupa
        fields = ['titulo_roupa', 'descricao_roupa', 'composicao_roupa', 'imagem_roupa', 'marca', 'modelo']

class LoginForms(forms.Form):
    email=forms.EmailField(
        label='Email', 
        required=True, 
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: leleo@leleo.com.br',
            }
        )
    )
    senha=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )