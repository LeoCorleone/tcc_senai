from django.db import models
from django.contrib.auth.models import User
import datetime


class Ano(models.Model):
    valor = models.IntegerField()

    def __str__(self):
        return str(self.valor)

class Colecao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Tipo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    titulo_produto = models.CharField(max_length=50)
    descricao_produto = models.CharField(max_length=250)
    composicao_produto = models.CharField(max_length=100)
    imagem_produto = models.ImageField(upload_to='uploads/')
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE)
    colecao = models.ForeignKey(Colecao, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    numero_comentarios = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    liked_by = models.ManyToManyField(User, blank=True, related_name='produtos_liked')

    def __str__(self):
        return self.titulo_produto

class Comentario(models.Model):
    texto = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="comentarios")
    data_publicacao = models.DateTimeField(auto_now_add=True)

class FaleConosco(models.Model):
    email = models.EmailField()
    mensagem = models.TextField()

    def __str__(self):
        return self.email
    
class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    

    
