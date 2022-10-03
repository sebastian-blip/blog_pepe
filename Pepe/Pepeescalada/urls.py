from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from .views import *


urlpatterns = [
    path('', feed, name='feed'),
    path('profile/', profile, name='profile'),
    path('profile/<str:username>/', profile, name='profile'),
    path('registro/', registro, name='registro'),
    path('editar/<str:user_id>', editar_perfil, name='editar'),
    path('ingreso/', LoginView.as_view(template_name='blog/ingreso.html'), name='ingreso'),
    path('salir/', LogoutView.as_view(template_name='blog/salir.html'), name='salir'),
    path('nuevoejercicio/', agregar_ejercicio, name='ejercicio'),
    path('rutina/eliminar/<int:ejercicio_id>', eliminar_ejercicio, name='eliminarejercicio'),
    path('Guardado/', guardado, name='guardado'),
    path('newpost/', nuevo_post, name='newpost'),
    path('eliminar/<int:post_id>', eliminar_post, name='eliminarpost'),
    path('noticia/', noticia, name='noticia'),
    path('noticia/<str:slug>/', noticia_detallada, name='detallenoticia'),
    path('crearnoticia/', nueva_noticia, name='crear_noticia'),
    path('noticia/eliminar/<str:noticia_id>', eliminar_noticia, name='eliminarnoticia'),
    path('follow/<str:username>/', follow, name='follow'),
    path('unfollow/<str:username>/', unfollow, name='unfollow'),
    path('rutina/<str:username>/', ver_ejercicio, name='mirutina'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)