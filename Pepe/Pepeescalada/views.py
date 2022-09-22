from django.shortcuts import render, redirect, get_object_or_404
from .models import Posteado, Ejercicio
from .forms import Registrousuario, EjercioForm, Nuevopost
from django.contrib import messages
from django.contrib.auth.models import User


def feed(request):
    mensajes = Posteado.objects.all()
    context = {'post': mensajes}
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


def profile(request):
    return render(request, 'blog/profile.html')


def guardado(request):
    return render(request, 'blog/Guardado.html')


def agregar_ejercicio(request):
    if request.method == 'POST':
        form = EjercioForm(request.POST)
        if form.is_valid():
            Ejercicio.objects.create(
                nombre_ejercicio=form.cleaned_data['nombre_ejercicio'],
                repeticiones=form.cleaned_data['repeticiones'],
                series=form.cleaned_data['series'],
            )
            messages.success(request, 'ejercicio guardado')
            return redirect('guardado')
    else:
        form = EjercioForm()
    return render(request, 'blog/registroEjercicio.html', {'form': form})


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

