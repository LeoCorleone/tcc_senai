from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import auth
from django.contrib.auth.models import User

def index(request):
    form = LoginForms()
    return render(request, 'index.html', {
        'form':form
    })

def login(request):
    form = LoginForms()

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
            return redirect('postagem')
        else:
            return redirect('login')

    return render(request, 'postagemform.html', {'form': form})

def adm(request):
    return render(request, 'adm.html')

def postagem(request):
  
    if request.method == 'POST':
        form = PostagemForms(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PostagemForms()
    return render(request, 'postagemform.html', {'form' : form})
