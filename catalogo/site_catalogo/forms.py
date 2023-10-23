from django import forms

class PostagemForms(forms.Form):
    titulo = forms.CharField(
        label = 'Titulo',
        required = True,
        max_length = 30,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Digite o titulo da postagem'
            }
        )
    )
    descricao = forms.CharField(
        label = 'Descrição',
        required = True,
        max_length = 200,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Digite a descrição da postagem'
            }
        )
    )
    imagem = forms.ImageField(
        
    )
