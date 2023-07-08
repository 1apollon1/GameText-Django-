import datetime

from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from mainapp.models import *
from .forms import *
from .utils import *


class ManageRoomOptions(UpdateView):
    template_name = 'chat/manage_room.html'

    extra_context = {'title': "Room's options"}

    def get_success_url(self):
        return reverse_lazy('show_room', kwargs={'room_id': self.object.pk})

    def get_object(self, queryset=None):
        return Rooms.objects.get(pk=self.kwargs['room_id'])

    def get_form_class(self):
        if self.request.user != self.object.author:
            raise PermissionError('You are not author of this room')
        return ManageRoomOptionsForm


@only_for_author
def manage_room_members(request, room_id):
    members = Membership.objects.filter(room=room_id).select_related()
    if request.method == 'POST':
        change_dict = get_change_dict(request)
        edit_members(change_dict)
        return redirect('show_room', room_id=room_id)
    else:
        return render(request, template_name='chat/manage_members.html', context={'members': members, 'room': members[0].room, 'title': "Room's members"})


def room(request, room_id):

    room = get_object_or_404(Rooms, pk = room_id)
    application_sent = False
    try:
        application = Application.objects.get(room=room, user=request.user)
        if get_days_delta(application.last_sent_date) < 4:
            application_sent=True
        elif 'send_application' in request.POST.keys():
            application.last_sent_date = datetime.datetime.now()
    except:
        if 'send_application' in request.POST.keys():
            Application.objects.create(room=room, user=request.user, application_sent=datetime.datetime.now())
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "chat/showroom.html", {"room": room, 'title': f'Room {room_id}', 'application_sent': application_sent})



def application(request, room_id):
    if request.user.pk in Membership.objects.filter(room_id=room_id).values_list('user', flat=True):
        raise ValidationError('You are member already')
    try:
        a1 = Application.objects.first()
        application = Application.objects.get(user_id=request.user.pk, room_id=room_id)
        if get_days_delta(application.last_sent_date) < 4:
            raise ValidationError('You applicated recently already')
        application.last_sent_date = datetime.now()
    except Application.DoesNotExist:
        Application.objects.create(user=request.user, room_id=room_id, last_sent_date = datetime.now())
    return redirect('show_room', room_id=room_id)

@only_for_author
def manage_applications(request, room_id):
    applications = Application.objects.filter(room=room_id).select_related()
    if request.method == 'POST':
        change_dict = get_change_dict(request)
        edit_members(change_dict)
        return redirect('manage_room_members', room_id=room_id)
    else:
        return render(request, template_name='chat/manage_applications.html', context={'applications': applications, 'room': applications[0].room, 'title': "Room's applications"})
