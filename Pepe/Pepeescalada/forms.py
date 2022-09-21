from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
