from django.shortcuts import render
from .models import Posteado


def feed(request):
    mensajes = Posteado.objects.all()
    context = {'post': mensajes}
    return render(request, 'blog/feed.html', context)


def profile(request):
    return render(request, 'blog/profile.html')
