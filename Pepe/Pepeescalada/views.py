from django.shortcuts import render, redirect
from .models import Posteado, Ejercicio
from .forms import Registrousuario, EjercioForm
from django.contrib import messages


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
