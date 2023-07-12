from django import forms
from mainapp.models import *

class ManageRoomOptionsForm(forms.ModelForm):
    c = []
    types = RoomType.objects.all()
    for t in types:
        c.append((t.pk, t.type_name))
    type = forms.ChoiceField(choices=c, widget=forms.Select(attrs={'class': 'creating_inputs', 'id': 'select_inp'}))
    class Meta:
        model = Rooms
        fields=[
            'room_name',
            'type',
            'chat_background_color',
            'action_chat_background_color',
            'chat_font_color',
            'action_chat_font_color',
            'chat_height',
            'chat_width',
            'action_chat_height',
            'action_chat_width',

        ]

    room_name = forms.CharField(label='Name for your room')


    chat_background_color = forms.CharField(
        label='Background color for your chatlog',
        widget=forms.TextInput(attrs={'type': 'color', 'class': 'manage-room-forms'})
    )

    action_chat_background_color = forms.CharField(
        label='Background color for your actionlog',
        widget=forms.TextInput(attrs={'type': 'color', 'class': 'manage-room-forms'})
    )

    chat_font_color =  forms.CharField(
        label='Font color for your chatlog',
        widget=forms.TextInput(attrs={'type': 'color', 'class': 'manage-room-forms'})
    )

    action_chat_font_color =  forms.CharField(
        label='Font color for your actionlog',
        widget=forms.TextInput(attrs={'type': 'color', 'class': 'manage-room-forms'})
    )



    chat_height = forms.IntegerField(
        label = 'Height for your chatlog',
        widget = forms.NumberInput(attrs={'style': "width: 50px;", 'min': 1, 'class': 'manage-room-forms'})
    )

    chat_width = forms.IntegerField(
        label='Width for your chatlog',
        widget = forms.NumberInput(attrs={'style': "width: 50px;", 'min': 1, 'class': 'manage-room-forms'})
    )

    action_chat_height = forms.IntegerField(
        label='Height for your actionlog',
        widget = forms.NumberInput(attrs={'style': "width: 50px;", 'min': 1, 'class': 'manage-room-forms'})
    )

    action_chat_width = forms.IntegerField(
        label='Width for your actionlog',
        widget = forms.NumberInput(attrs={'style': "width: 50px;", 'min': 1, 'class': 'manage-room-forms'})
    )


    def clean_type(self):
        return RoomType.objects.get(pk=int(self.cleaned_data['type']))
