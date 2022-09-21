from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from .views import feed, profile, registro


urlpatterns = [
    path('', feed, name='feed'),
    path('profile/', profile, name='profile'),
    path('registro/', registro, name='registro'),
    path('login/', LoginView.as_view(template_name='blog/ingreso.html'),
         name='ingreso')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)