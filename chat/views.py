from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from mainapp.models import *
from .forms import *


class ManageRoomOptions(UpdateView):
    template_name = 'chat/manage_room.html'
    success_url = reverse_lazy('get_to_main')


    def get_object(self, queryset=None):
        return Rooms.objects.get(pk=self.kwargs['room_id'])

    def get_form_class(self):
        if self.request.user != self.object.author:
            raise PermissionError('You are not author of this room')
        return ManageRoomOptionsForm






def room(request, room_id):
    room = get_object_or_404(Rooms, pk = room_id)
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "chat/showroom.html", {"room": room, 'title': f'Room {room_id}'})