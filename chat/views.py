from django.shortcuts import render

# Create your views here.
from django.shortcuts import render




def room(request, room_id):
    return render(request, "chat/showroom.html", {"room_name": room_id})