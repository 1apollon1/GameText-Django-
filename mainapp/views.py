from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404

def main(request):
    return HttpResponse('Hi dude')


def showrooms(request, room_page):
    if room_page > 5:
        raise Http404
    return HttpResponse(f'Here must be room {room_page}')
