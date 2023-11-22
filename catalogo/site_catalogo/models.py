from django.db import models
from django.contrib.auth.models import User

class Ano(models.Model):
    valor = models.IntegerField()

class Colecao(models.Model):
    nome = models.CharField(max_length=255)

class Tipo(models.Model):
    nome = models.CharField(max_length=255)

class Produto(models.Model):
    titulo_produto = models.CharField(max_length=50)
    descricao_produto = models.CharField(max_length=250)
    composicao_produto = models.CharField(max_length=100)
    imagem_produto = models.ImageField(upload_to='uploads/')
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE)
    colecao = models.ForeignKey(Colecao, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    liked_by = models.ManyToManyField(User, blank=True)


class Comentario(models.Model):
    texto = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="comentarios")
    data_publicacao = models.DateTimeField(auto_now_add=True)