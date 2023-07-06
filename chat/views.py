from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from mainapp.models import *
from .forms import *
from .utils import *


class ManageRoomOptions(UpdateView):
    template_name = 'chat/manage_room.html'


    def get_success_url(self):
        return reverse_lazy('show_room', kwargs={'room_id': self.object.pk})

    def get_object(self, queryset=None):
        return Rooms.objects.get(pk=self.kwargs['room_id'])

    def get_form_class(self):
        if self.request.user != self.object.author:
            raise PermissionError('You are not author of this room')
        return ManageRoomOptionsForm



def manage_room_members(request, room_id):
    members = Membership.objects.filter(room_id=room_id).select_related()
    if request.user != members[0].room.author:
        raise PermissionError('You are not author of this room')

    if request.method == 'POST':
        change_dict = get_change_dict(request)
        edit_members(change_dict)
        return redirect('show_room', room_id=room_id)
    else:
        return render(request, template_name='chat/manage_members.html', context={'members': members, 'room_id': members[0].room.pk})


def room(request, room_id):
    room = get_object_or_404(Rooms, pk = room_id)
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "chat/showroom.html", {"room": room, 'title': f'Room {room_id}'})


