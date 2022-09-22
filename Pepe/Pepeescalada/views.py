from django.shortcuts import render, redirect
from .models import Posteado
from .forms import Registrousuario
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
