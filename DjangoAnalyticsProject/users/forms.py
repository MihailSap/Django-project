from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django_recaptcha.fields import ReCaptchaField

User = get_user_model()


class UserCreationForm(UserCreationForm):
    captcha = ReCaptchaField()

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя'
    }))
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            'placeholder': 'Введите email'
        })
    )
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Придумайте пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Повторите пароль'
    }))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2", "captcha")


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

    class Meta(UserCreationForm.Meta):
        fields = ("username", "password")
