from django import forms
from .models import *

class PostagemForms(forms.Form):
    class Meta:
        model = Roupa
        fields = ['titulo_roupa', 'descricao_roupa', 'composicao_roupa', 'imagem_roupa', 'marca', 'modelo']