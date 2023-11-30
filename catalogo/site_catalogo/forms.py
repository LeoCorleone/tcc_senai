from django import forms
from .models import *

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['titulo_produto', 'descricao_produto', 'composicao_produto', 'ano', 'colecao', 'tipo', 'imagem_produto']




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

class FiltroForm(forms.Form):
    ano = forms.ModelChoiceField(queryset=Ano.objects.all(), empty_label="Selecione o Ano", required=False, label="Ano")
    colecao = forms.ModelChoiceField(queryset=Colecao.objects.all(), empty_label="Selecione a Coleção", required=False, label="Coleção")
    tipo = forms.ModelChoiceField(queryset=Tipo.objects.all(), empty_label="Selecione o Tipo", required=False, label="Tipo")

    def __init__(self, *args, **kwargs):
        super(FiltroForm, self).__init__(*args, **kwargs)
        self.fields['ano'].queryset = Ano.objects.all()
        self.fields['colecao'].queryset = Colecao.objects.all()
        self.fields['tipo'].queryset = Tipo.objects.all()