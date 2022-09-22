from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ejercicio, Posteado


class Registrousuario(UserCreationForm):

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': "controls"}))

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput
                                (attrs={'placeholder': 'Contraseña', 'class': "controls"})
                                )
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput
                                (attrs={'placeholder': 'Ingrese contraseña de nuevo',
                                        'class': "controls"})
                                )

    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Name', 'class': "controls"}),
        }
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {k: "" for k in fields}


class EjercioForm(forms.ModelForm):
    nombre_ejercicio = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={'rows': 2, 'placeholder': 'Nombre del ejercicio', 'class': "controls"}),
        required=True
    )
    repeticiones = forms.IntegerField(
        label="",
        widget=forms.Textarea(
            attrs={'rows': 2, 'placeholder': 'Repeticiones', 'class': "controls"}),
        required=True
    )
    series = forms.IntegerField(
        label="",
        widget=forms.Textarea(
            attrs={'rows': 2, 'placeholder': 'Series', 'class': "controls"}),
        required=True
    )

    class Meta:
        model = Ejercicio
        fields = ['nombre_ejercicio', 'repeticiones', 'series']


class Nuevopost(forms.ModelForm):

    contenido = forms.CharField(label="",
        widget=forms.Textarea(
            attrs={'rows': 2, 'placeholder': 'Que escalaste hoy', 'class': "controls"}),
        required=True)

    class Meta:
        model = Posteado
        fields = ['contenido']
