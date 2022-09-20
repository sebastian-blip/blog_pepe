from django.urls import path
from .views import feed, profile
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', feed, name='feed'),
    path('profile/', profile, name='profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)