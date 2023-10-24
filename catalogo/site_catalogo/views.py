from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

def index(request):
    return render(request, 'index.html')
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
  
  
def uploadok(request):
    return HttpResponse(' upload successful')
