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
    # descricao_modelo = models.CharField(max_length=250)

    def __str__(self):
        return self.nome_modelo

class Comentario(models.Model):
    texto = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    roupa = models.ForeignKey("Roupa", on_delete=models.CASCADE, related_name="comentarios")
    data_publicacao = models.DateTimeField(auto_now_add=True)

def exibir_comentario(request, roupa_id):
    roupa = get_object_or_404(Roupa, pk=roupa_id)
    comentarios = Comentario.objects.filter(roupa=roupa)
