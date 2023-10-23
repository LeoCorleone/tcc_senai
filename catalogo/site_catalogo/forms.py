from django import forms

class PostagemForms(forms.Form):
    clas Meta:
    model = Postagem
    fields = ['titulo', 'descricao', 'imagem']