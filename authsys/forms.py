from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.db.models import ObjectDoesNotExist
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from captcha.fields import CaptchaField


class SignUpForm(UserCreationForm):
    username = forms.CharField(strip=False)
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

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    avatar = forms.ImageField(
        label='Your avatar',
        widget=forms.FileInput(attrs={'accept': "image/png, image/gif, image/jpeg"}),
        required=False
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email', 'avatar']

    def clean_username(self):
        """Reject usernames that differ only in case."""
        username = self.cleaned_data.get("username")
        if (
            username
            and self._meta.model.objects.filter(username=username).exists()
        ):
            self._update_errors(
                ValidationError(
                    {
                        "username": self.instance.unique_error_message(
                            self._meta.model, ["username"]
                        )
                    }
                )
            )
        else:
            return username

    def clean_avatar(self):
        image = self.cleaned_data['avatar']
        if image and image.size//1024//1024 > 5:
            raise ValidationError('Too big image')
        return image

class SignInForm(AuthenticationForm):

    username = UsernameField(label='Login', widget=forms.TextInput(attrs={"autofocus": True}))

    error_messages = {
        "invalid_login": 'Wrong password or login',
        "inactive": ("This account is inactive."),
    }

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if not self.user_cache:
                try:
                    username = CustomUser.objects.get(email=username).username
                    self.user_cache = authenticate(
                        self.request, username=username, password=password
                    )
                except ObjectDoesNotExist:
                    pass

            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

class SignInFormSecurity(SignInForm):
    captcha = CaptchaField()

