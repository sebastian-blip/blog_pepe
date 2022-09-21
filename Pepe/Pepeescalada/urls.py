from django.urls import path
from .views import feed, profile, registro
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', feed, name='feed'),
    path('profile/', profile, name='profile'),
    path('registro/', registro, name='registro'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)