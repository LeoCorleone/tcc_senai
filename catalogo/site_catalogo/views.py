from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .forms import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test



def is_superuser(user):
    return user.is_authenticated and user.is_superuser

def index(request):
    formcomentario = ComentarioForm()
    filtro_form = FiltroForm(request.GET)
    form = LoginForms()

    postagem = Produto.objects.all()

    if filtro_form.is_valid():
        ano = filtro_form.cleaned_data.get('ano')
        colecao = filtro_form.cleaned_data.get('colecao')
        tipo = filtro_form.cleaned_data.get('tipo')

        if ano:
            postagem = postagem.filter(ano=ano)
        if colecao:
            postagem = postagem.filter(colecao=colecao)
        if tipo:
            postagem = postagem.filter(tipo=tipo)

    paginator = Paginator(postagem, 12)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        postagem = paginator.page(page)
    except (EmptyPage, InvalidPage):
        postagem = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'postagem': postagem, 'formcomentario': formcomentario, 'filtro_form': filtro_form, 'form': form})

def artdicas(request):
    form = LoginForms()
    return render(request, 'artdicas.html', {'form': form })

def sobre(request):
    form = LoginForms()
    return render(request, 'sobre.html', {'form': form})



def login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['senha']

            try:
                user = auth.authenticate(
                    request,
                    username=User.objects.get(email=email).username,
                    password=password
                )

                if user is not None:
                    auth.login(request, user)
                    messages.success(request, 'Foi logado com sucesso!')
                    return redirect('adm')
                else:
                    raise auth.AuthenticationFailed('Credenciais inválidas')

            except User.DoesNotExist:
                messages.error(request, 'E-mail não encontrado')
            except auth.AuthenticationFailed:
                messages.error(request, 'Credenciais inválidas')

    return redirect('index')

        
@login_required
def curtir_postagem(request, postagem_id):
    postagem = get_object_or_404(Produto, id=postagem_id)
    user = request.user
    
    if user in postagem.liked_by.all():
        postagem.liked_by.remove(user)
        postagem.likes -= 1
    else:
        postagem.liked_by.add(user)
        postagem.likes += 1

    postagem.save()
    return redirect('index')

@login_required
def adicionar_comentario(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.product = produto  # Alterado de 'produto' para 'product'
            comentario.save()

            produto.numero_comentarios += 1
            produto.save()

            return redirect('index')

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('index')

@user_passes_test(is_superuser)
def adm(request):
    return render(request, 'adm/adm.html')

@user_passes_test(is_superuser)
def postagem(request):
  
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            messages.success(request, f'Postagem criada com sucesso!')
            return redirect('listar_roupas')
    else:
        form = ProdutoForm()
    return render(request, 'adm/postagemform.html', {'form' : form})

@user_passes_test(is_superuser)
def listar_roupas(request):
    postagem = Produto.objects.all()
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

@user_passes_test(is_superuser)
def delete(request, id):
    produto = Produto.objects.get(pk=id)
    produto.delete()
    messages.success(request, f'Postagem deletada com sucesso!')
    return redirect('listar_roupas')

@user_passes_test(is_superuser)
def edit_roupa(request, id):
    produto = Produto.objects.get(pk=id)
    form = ProdutoForm(instance=produto)
    return render(request, "adm/updateroupa.html",{"form":form, "roupa":produto})

@user_passes_test(is_superuser)
def update_roupa(request, id):
    try:
        if request.method == "POST":
            photo = Produto.objects.get(pk=id)
            form = ProdutoForm(request.POST, request.FILES, instance=photo)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'postagem foi alterada com sucesso!')
                return redirect('listar_roupas')
    except Exception as e:
        messages.error(request, e)
        return redirect('listar_roupas')

@user_passes_test(is_superuser)
def adicionar_usuario(request):
    if request.method == "POST":
        form = CriarLoginForms(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['nome'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['senha']
            )

            if form.cleaned_data['is_admin']:
                user.is_superuser = True
                user.save()

            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('listar_usuario')
    else:
        form = CriarLoginForms()

    return render(request, "adm/addusuario.html", {
        'form': form
    })

@user_passes_test(is_superuser)
def listar_usuario(request):
    usuarios = User.objects.all()
    return render(request, 'adm/listagemusuarios.html', {
        'usuarios': usuarios
    })

@user_passes_test(is_superuser)
def delete_usuario(request, id):
    usuarios = User.objects.get(pk=id)
    usuarios.delete()
    messages.success(request, f'Usuario deletado com sucesso!')
    return redirect('listar_usuario')

@user_passes_test(is_superuser)
def update_usuario(request, id):
    usuario = User.objects.get(pk=id)
    if request.method == 'POST':
        usuario.username = request.POST['nome']
        usuario.set_password(request.POST['senha'])
        usuario.email = request.POST['email']
        usuario.save()
        return redirect('listar_usuario')
    return render(request, 'adm/editaruser.html', {'usuario': usuario})

@user_passes_test(is_superuser)
def inative(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    messages.success(request, 'Usuario inativado com sucesso!')
    return redirect('listar_usuario')

@user_passes_test(is_superuser)
def active(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    messages.success(request, 'Usuario ativado com sucesso!')
    return redirect('listar_usuario')

