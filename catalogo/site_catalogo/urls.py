from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

from django.conf.urls.static import static

from . import views 

urlpatterns = [
<<<<<<< HEAD
    path("", views.index, name="index"),
    path("adm/", views.adm, name= "adm"),
=======
    path("", index, name="index"),
    path("adm", adm, name= "adm"),
>>>>>>> ccc2c4e42d70d71e981c0d0dbd96bf83e3c05420
    path('postagem/', postagem, name = 'postagem'),
    path('login/', login, name='login')
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)