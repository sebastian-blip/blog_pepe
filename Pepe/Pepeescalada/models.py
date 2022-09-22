from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default='alien.jpg')

    def __str__(self):
        return f'Perfil de {self.user.username}'


class Posteado(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posteo')
    timestamp = models.DateTimeField(default=timezone.now)
    contenido = models.TextField()

    class Meta:
        ordering = ['-timestamp']


class Ejercicio(models.Model):
    nombre_ejercicio = models.CharField(max_length=100)
    repeticiones = models.IntegerField()
    series = models.IntegerField()



