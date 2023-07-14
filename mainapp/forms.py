from django import forms
from django.core.exceptions import ValidationError

from .models import *

class CreateRoom(forms.ModelForm):
    c = []
    types = RoomType.objects.all()
    for t in types:
        c.append((t.pk, t.type_name))
    type = forms.ChoiceField(choices=c, widget=forms.Select(attrs = {'class': 'creating_inputs', 'id': 'select_inp'}))
    class Meta:
        model = Rooms
        fields = ['room_name', 'type']
        widgets = {
            'room_name': forms.TextInput(attrs = {'class': 'creating_inputs'}),
        }

    def clean_type(self):
        return RoomType.objects.get(pk=int(self.cleaned_data['type']))


class Search(forms.Form):
    search_inp = forms.CharField(label='', widget=forms.TextInput(attrs={'style': 'width: 70%'}))