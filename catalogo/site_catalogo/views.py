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
            return redirect('listar_roupas')
    else:
        form = PostagemForms()
    return render(request, 'postagemform.html', {'form' : form})

def listar_roupas(request):
    postagem = Roupa.objects.all()
    return render(request, 'listagemroupas.html', {'postagem': postagem})

def delete(request, id):
    roupa = Roupa.objects.get(pk=id)
    roupa.delete()
    # messages.success(request, f'Postagem deletada com sucesso!')
    return redirect('listar_roupas')

def updateroupa(request, id):
    roupas = Roupa.objects.get(pk=id)
    if request.method == 'POST':
        roupas.titulo_roupa = request.POST['titulo_roupa']
        roupas.descricao_roupa = request.POST['descricao_roupa']
        roupas.composicao_roupa = request.POST['composicao_roupa']
        roupas.imagem_roupa = request.POST['imagem_roupa']
        roupas.marca = request.POST['marca']
        roupas.modelo = request.POST['modelo']
        roupas.save()
        # messages.success(request, f'Livro editado com sucesso!')
        return redirect('listagem')
    return render(request, "adm/editar.html",{'livro':roupas})

def adicionar_usuario(request):
    usuario = UsuarioForms()
    if request.method == "POST":
        cadastrouser = User.objects.create_user(
            username = request.POST['nome'], password = request.POST['password'],
                            email = request.POST['email'])
        cadastrouser.save()
        # messages.success(request, f'Usuario cadastrado com sucesso!')
        return redirect('listauser')

    return render(request, "adm/addusuario.html", {
        'form':usuario
    })

def listar_usuario(request):
    usuarios = User.objects.all()
    return render(request, 'listagemusuarios.html', {
        'usuarios': usuarios
    })

def delete_usuario(request, id):
    usuarios = User.objects.get(pk=id)
    usuarios.delete()
    # messages.success(request, f'Postagem deletada com sucesso!')
    return redirect('listar_usuario')

def update_usuario(request, id):
    usuario = User.objects.get(pk=id)
    if request.method == 'POST':
        usuario.username = request.POST['nome']
        usuario.set_password(request.POST['senha'])
        usuario.email = request.POST['email']
        usuario.save()
        return redirect('listagemusuario')
    return render(request, 'adm/editaruser.html', {'usuario': usuario})

def logout(request):
    auth.logout(request)
    # messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('index')
