from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField


class SignUpForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']


class SignInForm(AuthenticationForm):
    error_messages = {
        "invalid_login": 'Wrong password or login',
        "inactive": ("This account is inactive."),
    }

class SignInFormSecurity(SignInForm):
    captcha = CaptchaField()

