from django.db import models
from django.contrib.auth.models import User


class Roupa(models.Model):
    nome_roupa = models.CharField(max_length=50)
    descricao_roupa = models.CharField(max_length=250)
    composicao_roupa = models.CharField(max_length=100)
    foto_roupa = models.ImageField()
    marca = models.ForeignKey("Marca", on_delete=models.CASCADE, related_name='roupas')
    modelo = models.ForeignKey("Modelo", on_delete=models.CASCADE, related_name='roupas')

class Marca(models.Model):
    nome_marca = models.CharField(max_length=50)

class Modelo(models.Model):
    nome_modelo = models.CharField(max_length=50)
    descricao_modelo = models.CharField(max_length=250)

class UserRoupa(models.Model):
    curtida_roupa = models.IntegerField()
    comentario_roupa = models.TextField()
    usuario = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="usuario")
    roupa = models.ForeignKey(to=Roupa, on_delete=models.CASCADE, related_name="roupa")