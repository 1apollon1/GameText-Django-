from django.shortcuts import render
from .forms import *


# Create your views here.
from django.http import HttpResponse, Http404
from .models import *
from django.shortcuts import redirect

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


def create_room(request):
    forms = CreateRoom()
    if request.method == 'POST':
        forms = CreateRoom(request.POST)
        if forms.is_valid():
            try:
                Rooms.objects.create(**forms.cleaned_data)
                return redirect('get_to_main')
            except:
                forms.add_error(None, 'Error')
    context = {
        'Title': 'Room creating',
        'forms': forms
    }
    return render(request, 'mainapp/create_room.html', context=context)
