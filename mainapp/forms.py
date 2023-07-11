from django import forms
from django.core.exceptions import ValidationError

from .models import *

class CreateRoom(forms.ModelForm):

    class Meta:
        model = Rooms
        fields = ['room_name', 'type']
        widgets = {
            'room_name': forms.TextInput(attrs = {'class': 'creating_inputs'}),
            'type': forms.Select(attrs={'class': 'creating_inputs', 'id': 'select_inp'}),
        }

    def clean_room_name(self):
        errors = []
        room_name = self.cleaned_data['room_name']
        if room_name.lower().__contains__('fuck'):
            errors.append(ValidationError('No swearing in room name'))
        if errors:
            raise ValidationError(errors)
        else:
            return room_name

