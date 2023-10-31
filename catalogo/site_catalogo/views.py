from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Roupa
from .forms import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

def index(request):
    form = LoginForms()
    postagem = Roupa.objects.all()
    return render(request, 'index.html', {'form': form, 'postagem': postagem})

def login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            email = form['email'].value()
            password = form['senha'].value()
        user_temp = User.objects.get(email= email)

        user = auth.authenticate(
            request,
            username=user_temp,
            password=password
        )

        if user is not None:
            auth.login(request, user)
            # messages.success(request, f'Foi logado com sucesso!')
            return redirect('postagem')
        else:
            # messages.error(request, 'Erro ao efetuar login')
            return redirect('index')

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

def listar_roupas(request):
    postagem = Roupa.objects.all()
    return render(request, 'listagemroupas.html', {'postagem': postagem})


