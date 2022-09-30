from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test, login_required


def feed(request):
    mensajes = Posteado.objects.all()
    context = {'posts': mensajes}
    return render(request, 'blog/feed.html', context)


def registro(request):
    if request.method == 'POST':
        form = Registrousuario(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} registrado')
            return redirect('feed')
    else:
        form = Registrousuario()

    context = {'form': form}
    return render(request, 'blog/registro.html', context)


def profile(request, username=None):
    current_user = request.user
    if username and username != current_user:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user

    context = {'user': user, 'posts': posts}
    return render(request, 'blog/profile.html', context)


def guardado(request):
    return render(request, 'blog/Guardado.html')


@login_required
def agregar_ejercicio(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = EjercioForm(request.POST)
        if form.is_valid():
            Ejercicio.objects.create(
                nombre_ejercicio=form.cleaned_data['nombre_ejercicio'],
                repeticiones=form.cleaned_data['repeticiones'],
                series=form.cleaned_data['series'],
                user=current_user
            )
            messages.success(request, 'ejercicio guardado')
            return redirect('guardado')
    else:
        form = EjercioForm()
    return render(request, 'blog/registroEjercicio.html', {'form': form})


@login_required
def ver_ejercicio(request, username=None):
    current_user = request.user
    if username and username != current_user:
        user = User.objects.get(username=username)
        ejercicios = user.ejercicio.all()
    else:
        ejercicios = current_user.ejercicio.all()
        user = current_user

    context = {'user': user, 'ejercicios': ejercicios}
    return render(request, 'blog/ejercicios.html', context)


@login_required
def nuevo_post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = Nuevopost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'post nuevo')
            return redirect('feed')
    else:
        form = Nuevopost()
    return render(request, 'blog/posteo.html', {'form': form})


def noticia(request):
    mensajes = Publicacion.objects.all()
    context = {'posts': mensajes}
    return render(request, 'blog/noticias.html', context)


def noticia_detallada(request, slug=None):

    post = Publicacion.objects.get(slug=slug)
    context = {'post': post}
    return render(request, 'blog/noticia_detallada.html', context)


@user_passes_test(lambda u: u.is_superuser)
def nueva_noticia(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = Nuevanoticia(request.POST, request.FILES)
        if form.is_valid():
            post = Publicacion.objects.create(
                title=form.cleaned_data["title"],
                body=form.cleaned_data["body"],
                image=form.cleaned_data["image"],
                state=form.cleaned_data["state"],
                autor=current_user,
                tags=form.cleaned_data["tags"],
                slug=form.cleaned_data["slug"]
            )

            post.save()
            messages.success(request, 'post nuevo')
            return redirect('noticia')
    else:
        form = Nuevanoticia()
    return render(request, 'blog/nuevanoticia.html', {'form': form})


@login_required
def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relacion(from_user=current_user, to_user=to_user_id)
    rel.save()
    messages.success(request, f'Ahora sigues a {username}')
    return redirect('profile')


@login_required
def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relacion.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    messages.success(request, f'Ya no sigues a {username}')
    return redirect('profile')
