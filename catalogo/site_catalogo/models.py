from django.db import models

# Create your models here.

class Postagem(models.Model):
    titulo = models.Charfield(max_length=30)
    descricao = models.Charfield(max_length=200)
    imagem = models.ImageFiel(upload_to='uploads/')

