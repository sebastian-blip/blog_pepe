from django.urls import path
from .views import feed, profile

urlpatterns = [
    path('', feed, name='feed'),
    path('profile/', profile, name='profile')
]