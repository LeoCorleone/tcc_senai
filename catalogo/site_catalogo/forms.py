from django import forms

class PostagemForms(forms.Form):
    class Meta:
        model = Postagem
        fields = ['titulo', 'descricao', 'imagem']