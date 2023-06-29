from django.db import models
from django.contrib import admin
from django.shortcuts import reverse
from authsys.models import CustomUser

class RoomType(models.Model):
    type_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.type_name
my_own_errors = {
    'unique': 'Such name taken already'

}
class Rooms(models.Model):
    room_name = models.CharField(max_length=100, unique=True, db_index=True, error_messages=my_own_errors)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    type = models.ForeignKey(RoomType, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.room_name
    def get_output_address(self):
        return reverse('show_room', kwargs={'room_id': self.pk})
    def get_user_address(self):
        return reverse('show_user', kwargs={'userid': 0})

    class Meta:
        verbose_name_plural = "rooms"

admin.site.register(RoomType)

# Create your models here.
