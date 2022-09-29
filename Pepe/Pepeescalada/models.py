from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from ckeditor.fields import RichTextField


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default='alien.jpg')

    def __str__(self):
        return f'Perfil de {self.user.username}'


class Posteado(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    contenido = models.TextField()

    class Meta:
        ordering = ['-timestamp']


class Ejercicio(models.Model):
    nombre_ejercicio = models.CharField(max_length=100)
    repeticiones = models.IntegerField()
    series = models.IntegerField()


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Publicacion(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField()
    image = models.ImageField(upload_to="noticas", default="alien.jpg")
    state = models.BooleanField('Active/no publicado', default=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publicaciones')
    tags = models.ForeignKey(Tag, on_delete=models.PROTECT, default=1)
    timestamp = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250, null=False, unique=True, default=1)

    class Meta:
        verbose_name = 'publicacion'
        verbose_name_plural = 'publicaciones'
        ordering = ['-timestamp']

    def __str__(self):
        return self.title


