from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['titulo_produto', 'descricao_produto', 'composicao_produto', 'ano', 'colecao', 'tipo', 'imagem_produto']


class ComentarioForm(forms.Form):
    comentario_roupa = forms.CharField(widget=forms.Textarea)

class LoginForms(forms.Form):
    email = forms.EmailField(
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
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        )
    )

class CriarLoginForms(forms.Form):
    nome = forms.CharField(
        label='Nome Completo',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control my-custom-input',
                'placeholder': 'Digite seu nome',
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control my-custom-input',
                'placeholder': 'Ex.: leleo@leleo.com.br',
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control my-custom-input',
                'placeholder': 'Digite a sua senha',
            }
        )
    )
    is_admin = forms.BooleanField(
        label='Administrador?',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input my-custom-checkbox',
            }
        )
    )

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.TextInput(attrs={'placeholder': 'Digite seu comentário...'}),
        }