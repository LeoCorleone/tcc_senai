from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

from django.conf.urls.static import static

from . import views 

urlpatterns = [
    path("", index, name="index"),
    path("adm", adm, name= "adm"),
    path('postagem/', postagem, name = 'postagem'),
    path('login/', login, name='login')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)