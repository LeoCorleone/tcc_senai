from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Roupa(models.Model):
    titulo_roupa = models.CharField(max_length=50)
    descricao_roupa = models.CharField(max_length=250)
    composicao_roupa = models.CharField(max_length=100)
    imagem_roupa = models.ImageField(upload_to='uploads/')
    marca = models.ForeignKey("Marca", on_delete=models.CASCADE, related_name='roupas')
    modelo = models.ForeignKey("Modelo", on_delete=models.CASCADE, related_name='roupas')
    likes = models.PositiveIntegerField(default=0)
    liked_by = models.ManyToManyField(User, blank=True)

    
class Marca(models.Model):
    nome_marca = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_marca

class Modelo(models.Model):
    nome_modelo = models.CharField(max_length=50)
    descricao_modelo = models.CharField(max_length=250)

    def __str__(self):
        return self.nome_modelo

class UserRoupa(models.Model):
    curtida_roupa = models.IntegerField()
    comentario_roupa = models.TextField()
    usuario = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="usuario")
    roupa = models.ForeignKey(to=Roupa, on_delete=models.CASCADE, related_name="roupa")

class Mensagem(models.Model):
    roupa = models.ForeignKey(Roupa, on_delete=models.CASCADE)
    remetente = models.ForeignKey(User, on_delete=models.CASCADE)  # Suponha que você tenha um modelo User
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

