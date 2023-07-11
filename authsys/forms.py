from django import forms
from django.core.exceptions import ValidationError

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

    avatar = forms.ImageField(
        label='Your avatar',
        widget=forms.FileInput(attrs={'accept': "image/png, image/gif, image/jpeg"}),
        required=False
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'avatar']


    def clean_avatar(self):
        image = self.cleaned_data['avatar']
        if image and image.size//1024//1024 > 5:
            raise ValidationError('Too big image')
        return image

class SignInForm(AuthenticationForm):
    error_messages = {
        "invalid_login": 'Wrong password or login',
        "inactive": ("This account is inactive."),
    }

class SignInFormSecurity(SignInForm):
    captcha = CaptchaField()

