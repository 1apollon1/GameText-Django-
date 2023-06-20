from django.contrib.auth.mixins import LoginRequiredMixin
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
    paginate_by = 10
    model = Rooms
    context_object_name = 'rooms'
    template_name = 'mainapp/showrooms.html'
    extra_context = {'title': 'Main'}
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['types'] = RoomType.objects.all()
        return context
    def get_queryset(self):
        if 'typid' in self.request.GET.keys() and self.request.GET['typid'].isdigit():
            queryset = Rooms.objects.filter(type_id = int(self.request.GET['typid']))
        else:
            queryset = Rooms.objects.all()
        queryset = queryset.order_by('-create_date')
        return queryset



class ShowRoom(DetailView):
    model = Rooms
    context_object_name = 'room'
    pk_url_kwarg = 'roomid'
    template_name = 'mainapp/room.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = self.get_object().room_name
        return context



def show_user(request, userid):
    return HttpResponse('User')





class CreateRoomView(LoginRequiredMixin, CreateView):
    model = Rooms
    template_name = 'mainapp/create_room.html'
    form_class = CreateRoom
    login_url = 'login'
    extra_context = {'title': 'Create room page'}

    def form_valid(self, form):
        room = form.save(commit=False)
        room.author = self.request.user
        room.save()
        self.success_url = reverse_lazy('get_to_main')
        return super(CreateRoomView, self).form_valid(form)



def login(request):
    return HttpResponse('Login')
