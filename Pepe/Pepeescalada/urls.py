from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from .views import feed, profile, registro


urlpatterns = [
    path('', feed, name='feed'),
    path('profile/', profile, name='profile'),
    path('registro/', registro, name='registro'),
    path('ingreso/', LoginView.as_view(template_name='blog/ingreso.html'),
         name='ingreso'),
    path('salir/', LogoutView.as_view(template_name='blog/salir.html'),
         name='salir')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)