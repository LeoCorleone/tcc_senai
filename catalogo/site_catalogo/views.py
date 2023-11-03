from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Roupa, Mensagem
from .forms import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


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

# def updateroupa(request, id):
#     roupas = Roupa.objects.get(pk=id)
#     if request.method == 'POST':
#         roupas.titulo_roupa = request.POST['titulo_roupa']
#         roupas.descricao_roupa = request.POST['descricao_roupa']
#         roupas.composicao_roupa = request.POST['composicao_roupa']
#         roupas.imagem_roupa = request.POST['imagem_roupa']
#         roupas.marca = request.POST['marca']
#         roupas.modelo = request.POST['modelo']
#         roupas.save()
#         # messages.success(request, f'Livro editado com sucesso!')
#         return redirect('listar_roupas')
#     return render(request, "updateroupa.html",{'roupas':roupas})
# @login_required
def edit_roupa(request, id):
    roupa = Roupa.objects.get(pk=id)
    form = PostagemForms(instance=roupa)
    return render(request, "updateroupa.html",{"form":form, "roupa":roupa})

# @login_required
def update_roupa(request, id):
    try:
        if request.method == "POST":
            photo = Roupa.objects.get(pk=id)
            form = PostagemForms(request.POST, request.FILES, instance=photo)
            
            if form.is_valid():
                form.save()
                # messages.success(request, 'postagem foi alterada com sucesso!')
                return redirect('listar_roupas')
    except Exception as e:
        # messages.error(request, e)
        return redirect('listar_roupas')

def adicionar_usuario(request):
    usuario = LoginForms()
    if request.method == "POST":
        cadastrouser = User.objects.create_user(
            username = request.POST['nome'], password = request.POST['senha'],
                            email = request.POST['email'])
        cadastrouser.save()
        # messages.success(request, f'Usuario cadastrado com sucesso!')
        return redirect('listar_usuario')

    return render(request, "addusuario.html", {
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

#                 # Certifique-se de que o usuário esteja autenticado
def curtir_postagem(request, postagem_id):
    postagem = get_object_or_404(Roupa, id=postagem_id)
    user = request.user

    if user in postagem.liked_by.all():
        # O usuário já curtiu a postagem, então vamos remover a curtida
        postagem.liked_by.remove(user)
        postagem.likes -= 1
    else:
        # O usuário não curtiu a postagem, vamos adicionar a curtida
        postagem.liked_by.add(user)
        postagem.likes += 1

    postagem.save()
    return redirect('index')
