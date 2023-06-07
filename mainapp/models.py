from django.db import models
from django.contrib import admin

class Rooms(models.Model):
    room_name = models.CharField(max_length=100)
    room_author_name = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.room_name

admin.site.register(Rooms)

# Create your models here.
