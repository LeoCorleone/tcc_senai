from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

from django.conf.urls.static import static

from . import views 

urlpatterns = [

    path("", index, name="index"),
    path("artdicas/", artdicas, name="artdicas"),
    path("sobre/", sobre, name="sobre"),
    path("adm/", adm, name= "adm"),
    path('postagem/', postagem, name = 'postagem'),
    path('login', login, name='login'),
    path('logout/', logout, name='logout'),
    path('deletar/<int:id>', delete, name="delete"),
    path('listarroupas/', listar_roupas, name='listar_roupas'),
    path('imagem/edit/<int:id>', edit_roupa, name="edit_roupa"),
    path('imagem/update/<int:id>', update_roupa, name="update_roupa"),
    path('listarusuario', listar_usuario, name='listar_usuario'),
    path('adicionarusuario', adicionar_usuario, name='adicionar_usuario'),
    path('editarusuario/<int:id>', update_usuario, name='editar_usuario'),
    path('updateusuario/<int:id>', update_usuario, name='update_usuario'),
    path('inativar/<int:id>', inative, name="inative_user"),
    path('ativar/<int:id>', active, name="active_user"),
    path('curtir/<int:postagem_id>/', curtir_postagem, name='curtir_postagem'),
    path('index/<int:produto_id>/adicionar_comentario/', adicionar_comentario, name='adicionar_comentario'),
    # path('index/<int:roupa_id>/exibir', exibir_comentario, name='exibir_comentario'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)