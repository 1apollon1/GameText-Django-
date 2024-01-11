from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from django.utils.html import mark_safe
from MagrasBox.settings import BASE_DIR



class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', verbose_name="User's avatar", default='avatars/avatar.jpg')
    email = models.EmailField(("email address"), blank=True, unique=True)

    def avatar_tag(self):
        if self.avatar:
            return mark_safe(f'<img src="/media/{self.avatar}" width="150" height="150" />')
        else:
            return 'No media'
    avatar_tag.short_description = 'Image for avatar'
# Create your models here.
