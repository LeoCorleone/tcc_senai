from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

from django.conf.urls.static import static

from . import views 

urlpatterns = [

    path("", index, name="index"),
    path("adm/", adm, name= "adm"),
    path('postagem/', postagem, name = 'postagem'),
    path('login', login, name='login'),
    path('logout/', logout, name='logout'),
    path('deletar/<int:id>', delete, name="delete"),
    path('listarroupas/', listar_roupas, name='listar_roupas'),
    path('editar/<int:id>', updateroupa, name="editar_roupa"),
    path('update/<int:id>', updateroupa, name='update_roupa'),
    path('listarusuario', listar_usuario, name='lista_usuario'),
    path('adicionarusuario', adicionar_usuario, name='adicionar_usuario'),
    path('deleteusuario/<int:id>', delete_usuario, name='delete_usuario'),
    path('editarusuario/<int:id>', update_usuario, name='editar_usuario'),
    path('updateusuario/<int:id>', update_usuario, name='update_roupa'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)