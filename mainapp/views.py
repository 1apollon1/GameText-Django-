from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
from django.http import HttpResponse, Http404
from .models import *
from django.shortcuts import redirect

class Main(ListView):
    model = Rooms
    context_object_name = 'rooms'
    template_name = 'mainapp/showrooms.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['types'] = RoomType.objects.all()
        return context
    def get_queryset(self):
        print(self.request.GET.keys())
        if 'typid' in self.request.GET.keys() and self.request.GET['typid'].isdigit():
            queryset = Rooms.objects.filter(type_id = int(self.request.GET['typid']))
        else:
            queryset = Rooms.objects.all()
        return queryset



class ShowRoom(DetailView):
    model = Rooms
    context_object_name = 'room'
    pk_url_kwarg = 'roomid'
    template_name = 'mainapp/room.html'



def show_user(request, userid):
    return HttpResponse('User')





class CreateRoomView(CreateView):
    model = Rooms
    template_name = 'mainapp/create_room.html'
    form_class = CreateRoom
    success_url = reverse_lazy('get_to_main')
