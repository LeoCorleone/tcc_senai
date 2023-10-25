from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Roupa
from .forms import *
from django.contrib import auth
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def adm(request):
    return render(request, 'adm.html')

def postagem(request):
  
    if request.method == 'POST':
        form = PostagemForms(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    else:
        form = PostagemForms()
    return render(request, 'postagemform.html', {'form' : form})
