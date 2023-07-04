from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import FormView

from mainapp.models import *


def room(request, room_id):
    room = get_object_or_404(Rooms, pk = room_id)
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "chat/showroom.html", {"room": room, 'title': f'Room {room_id}'})