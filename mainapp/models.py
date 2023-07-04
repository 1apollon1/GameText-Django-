from django.db import models
from django.contrib import admin
from django.shortcuts import reverse
from authsys.models import CustomUser
from os import remove
from MagrasBox.settings import BASE_DIR




class RoomType(models.Model):
    type_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.type_name
my_own_errors = {
    'unique': 'Such name taken already'

}
class Rooms(models.Model):
    room_name = models.CharField(max_length=100, unique=True, db_index=True, error_messages=my_own_errors)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, related_name='created_posts')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    type = models.ForeignKey(RoomType, on_delete=models.SET_DEFAULT, default=1)
    members = models.ManyToManyField(CustomUser, through='Membership')

    def __str__(self):
        return self.room_name
    def get_output_address(self):
        return reverse('show_room', kwargs={'room_id': self.pk})
    def get_user_address(self):
        return reverse('show_user', kwargs={'userid': 0})

    def delete(self, using=None, keep_parents=False):
        path_t = f"{BASE_DIR}/chat/chats_data/{self.pk}.txt"
        path_a = f"{BASE_DIR}/chat/actions_data/{self.pk}.txt"
        remove(path_t)
        remove(path_a)
        super().delete(using=None, keep_parents=False)





    class Meta:
        verbose_name_plural = "rooms"


class Membership(models.Model):
    room_id = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, default='With no role')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['room_id', 'user_id'], name='unique_membership')
        ]

admin.site.register(RoomType)

# Create your models here.
