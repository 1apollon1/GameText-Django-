from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from .models import *

def main(request):
    room = Rooms.objects.get(pk = 3)
    return render(request, 'mainapp/main.html', {'title': 'Main Page'})

def showrooms(request, room_page):
    rooms = Rooms.objects.all()
    if room_page > len(rooms):
        raise Http404
    return render(request, 'mainapp/showrooms.html', {'title': "Room List", 'page': room_page, 'rooms': rooms[:room_page]})
