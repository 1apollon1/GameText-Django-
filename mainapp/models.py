from django.db import models
from django.contrib import admin
from django.shortcuts import reverse


class RoomType(models.Model):
    type_name = models.CharField(max_length=100, unique=True)

class Rooms(models.Model):
    room_name = models.CharField(max_length=100, unique=True, db_index=True)
    room_author_name = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    type = models.ForeignKey(RoomType, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.room_name
    def get_output_address(self):
        return reverse('show_room', kwargs={'pageid': self.pk})

    class Meta:
        verbose_name_plural = "rooms"

admin.site.register(Rooms)
admin.site.register(RoomType)

# Create your models here.
