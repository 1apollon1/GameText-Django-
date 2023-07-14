from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .forms import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormMixin
from MagrasBox.settings import BASE_DIR
import os

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


    def get(self, request, *args, **kwargs):
        self.query = {}
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.query = {}
        if 'search_inp' in self.request.POST:
            self.query['room_name__contains'] = request.POST.get('search_inp')
        else:
            del self.query['room_name__contains']
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['types'] = RoomType.objects.all()
        if 'search_inp' in self.request.POST:
            context['search_init'] = self.request.POST.get('search_inp')
        return context


    def get_queryset(self):
        if 'typid' in self.request.GET.keys() and self.request.GET['typid'].isdigit():
            self.query['type_id'] = int(self.request.GET['typid'])
        if self.query != {}:
            queryset = Rooms.objects.filter(**self.query).select_related('author', 'type').order_by('-create_date')
        else:
            queryset = Rooms.objects.all().select_related('author', 'type').order_by('-create_date')
        return queryset



class ShowRoom(DetailView):
    model = Rooms
    pk_url_kwarg = 'roomid'
    template_name = 'mainapp/room.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = self.object.room_name
        return context



def show_user(request, userid):
    return HttpResponse('User')


def delete_room(request, room_id):
    room =  get_object_or_404(Rooms, pk = room_id)
    if request.user != room.author:
        raise PermissionError('You are not author of this room')
    else:
        room.delete()
        return redirect('get_to_main')



class CreateRoomView(LoginRequiredMixin, CreateView):
    model = Rooms
    template_name = 'mainapp/create_room.html'
    login_url = 'login'
    form_class = CreateRoom
    extra_context = {'title': 'Create room page'}

    def create_data(self, room):
        path_t = f"{BASE_DIR}/chat/chats_data/"
        path_a = f"{BASE_DIR}/chat/actions_data/"

        if not os.path.exists(path_t):
            os.makedirs(path_t)
        if not os.path.exists(path_a):
            os.makedirs(path_a)


        with open(f'{path_t}{room.pk}.txt', "w") as f:
            f.write("Welcome\n")
        with open(f'{path_a}{room.pk}.txt', "w") as f:
            f.write("")


    def form_valid(self, form):
        room = form.save(commit=False)
        room.author = self.request.user
        room.save()
        Membership.objects.create(room = room, user = self.request.user, can_write=True)
        self.success_url = reverse_lazy('get_to_main')
        self.create_data(room)
        return super(CreateRoomView, self).form_valid(form)



