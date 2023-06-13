from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from .models import *

def main(request):
    rooms = Rooms.objects.all()
    types = RoomType.objects.all()
    if 'typid' in request.GET.keys() and request.GET['typid'].isdigit():
        rooms = Rooms.objects.filter(type_id=int(request.GET['typid']))
    context = {
        'Title': 'Main Page',
        'rooms': rooms,
        'types': types
    }
    return render(request, 'mainapp/showrooms.html',context=context)

def showroom(request, pageid):
    room = Rooms.objects.get(id = pageid)
    context = {
        'Title': room.room_name,
        'room': room
    }
    return render(request, 'mainapp/room.html', context=context)

def show_user(request, userid):
    return HttpResponse('User')

