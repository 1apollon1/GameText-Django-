from django import forms
from .models import *

class CreateRoom(forms.Form):
    room_name = forms.CharField(max_length='50', label = 'Name for your room' )
    room_author_name = forms.CharField(max_length='50')
    type = forms.ModelChoiceField(queryset = RoomType.objects.all())
