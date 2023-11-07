from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Roupa, Comentario
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .forms import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    form = LoginForms()
    postagem = Roupa.objects.all()
    paginator = Paginator(postagem, 6) 
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        postagem = paginator.page(page)
    except (EmptyPage, InvalidPage):
        postagem = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'form': form, 'postagem': postagem})

def indexlogin(request):
    postagem = Roupa.objects.all()
    paginator = Paginator(postagem, 6) 
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        postagem = paginator.page(page)
    except (EmptyPage, InvalidPage):
        postagem = paginator.page(paginator.num_pages)
    return render(request, 'adm/indexlogin.html', {'postagem': postagem})

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
            messages.success(request, f'Foi logado com sucesso!')
            return redirect('indexlogin')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('index')

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('index')

def adm(request):
    return render(request, 'adm/adm.html')

def postagem(request):
  
    if request.method == 'POST':
        form = PostagemForms(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            messages.success(request, f'Postagem criada com sucesso!')
            return redirect('listar_roupas')
    else:
        form = PostagemForms()
    return render(request, 'adm/postagemform.html', {'form' : form})

def listar_roupas(request):
    postagem = Roupa.objects.all()
    paginator = Paginator(postagem, 6) 
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        postagem = paginator.page(page)
    except (EmptyPage, InvalidPage):
        postagem = paginator.page(paginator.num_pages)
    return render(request, 'adm/listagemroupas.html', {'postagem': postagem})

def delete(request, id):
    roupa = Roupa.objects.get(pk=id)
    roupa.delete()
    messages.success(request, f'Postagem deletada com sucesso!')
    return redirect('listar_roupas')

def edit_roupa(request, id):
    roupa = Roupa.objects.get(pk=id)
    form = PostagemForms(instance=roupa)
    return render(request, "adm/updateroupa.html",{"form":form, "roupa":roupa})

def update_roupa(request, id):
    try:
        if request.method == "POST":
            photo = Roupa.objects.get(pk=id)
            form = PostagemForms(request.POST, request.FILES, instance=photo)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'postagem foi alterada com sucesso!')
                return redirect('listar_roupas')
    except Exception as e:
        messages.error(request, e)
        return redirect('listar_roupas')

def adicionar_usuario(request):
    usuario = CriarLoginForms()
    if request.method == "POST":
        cadastrouser = User.objects.create_user(
            username = request.POST['nome'], password = request.POST['senha'],
                            email = request.POST['email'])
        cadastrouser.save()
        messages.success(request, f'Usuario cadastrado com sucesso!')
        return redirect('listar_usuario')

    return render(request, "adm/addusuario.html", {
        'form':usuario
    })

def listar_usuario(request):
    usuarios = User.objects.all()
    return render(request, 'adm/listagemusuarios.html', {
        'usuarios': usuarios
    })

def delete_usuario(request, id):
    usuarios = User.objects.get(pk=id)
    usuarios.delete()
    messages.success(request, f'Usuario deletado com sucesso!')
    return redirect('listar_usuario')

def update_usuario(request, id):
    usuario = User.objects.get(pk=id)
    if request.method == 'POST':
        usuario.username = request.POST['nome']
        usuario.set_password(request.POST['senha'])
        usuario.email = request.POST['email']
        usuario.save()
        return redirect('listar_usuario')
    return render(request, 'adm/editaruser.html', {'usuario': usuario})

def inative(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    messages.success(request, 'Usuario inativado com sucesso!')
    return redirect('listar_usuario')


def active(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    messages.success(request, 'Usuario ativado com sucesso!')
    return redirect('listar_usuario')


def curtir_postagem(request, postagem_id):
    postagem = get_object_or_404(Roupa, id=postagem_id)
    user = request.user
    
    if user in postagem.liked_by.all():
        postagem.liked_by.remove(user)
        postagem.likes -= 1
    else:
        postagem.liked_by.add(user)
        postagem.likes += 1

    postagem.save()
    return redirect('index')

def adicionar_comentario(request, roupa_id):
    roupa = get_object_or_404(Roupa, pk=roupa_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.roupa = roupa
            comentario.save()
            return redirect('index.html', roupa_id=roupa_id)
    else:
        form = ComentarioForm()

    return render(request, 'index.html', {'form': form})

def exibir_comentario(request, roupa_id):
    roupa = get_object_or_404(Roupa, pk=roupa_id)
    comentarios = Comentario.objects.filter(roupa=roupa)