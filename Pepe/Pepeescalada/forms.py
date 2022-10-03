from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from ckeditor.fields import RichTextFormField
from ckeditor.widgets import CKEditorWidget


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


class EditProfileForm(forms.ModelForm):

    imagen = forms.ImageField(label='Profile Picture', required=False, widget=forms.FileInput)

    class Meta:
        model = Perfil
        fields = ('imagen',)


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


class Nuevanoticia(forms.ModelForm):
    tages = Tag.objects.all().values_list("name")
    choise = [tage for tage in tages]

    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )
    slug = forms.SlugField(label="",  widget=forms.TextInput(
            attrs={'placeholder': 'Slug'}))
    title = forms.CharField(label="",  widget=forms.TextInput(
            attrs={'placeholder': 'title'}))
    state = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, label="Publicar",
                              initial='', widget=forms.Select(), required=True)
    image = forms.ImageField()
    tags = forms.Select(choices=choise)
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Publicacion
        fields = ['title', 'body', 'image', 'tags', 'state', 'slug', ]

