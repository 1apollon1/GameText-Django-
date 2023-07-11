import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from mainapp.models import *
from .forms import *
from .utils import *




class ManageRoomOptions(LoginRequiredMixin,UpdateView):
    template_name = 'chat/manage_room.html'
    login_url = reverse_lazy('login')
    extra_context = {'title': "Room's options"}

    def get_success_url(self):
        return reverse_lazy('show_room', kwargs={'room_id': self.object.pk})

    def get_object(self, queryset=None):
        return Rooms.objects.get(pk=self.kwargs['room_id'])

    def get_form_class(self):
        if self.request.user != self.object.author:
            raise PermissionError('You are not author of this room')
        return ManageRoomOptionsForm




@login_required
@only_for_author
def manage_room_members(request, room_id):
    members = Membership.objects.filter(room=room_id).select_related()
    if request.method == 'POST':
        change_dict = get_change_dict(request)
        edit_members(change_dict)
        return redirect('show_room', room_id=room_id)
    else:
        return render(request, template_name='chat/manage_members.html', context={'members': members, 'rid': room_id, 'title': "Room's members"})





@login_required
def room(request, room_id):

    room = get_object_or_404(Rooms, pk = room_id)
    application_sent = False
    try:
        application = Application.objects.get(room=room, user=request.user)
        application_sent = True
        if application.was_rejected and get_days_delta(application.reject_date) >= 4:
            application_sent=False
    except Application.DoesNotExist:
        pass
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        member = Membership.objects.get(room_id=room_id, user_id=request.user.pk)
    except Membership.DoesNotExist:
        member = None
    return render(request, "chat/showroom.html", {"room": room, 'title': f'Room {room_id}', 'application_sent': application_sent, 'member': member})






@login_required
def application_send(request, room_id):
    if request.user.pk in Membership.objects.filter(room_id=room_id).values_list('user', flat=True):
        raise Exception('You are member already')
    try:
        application = Application.objects.get(user_id=request.user.pk, room_id=room_id)
        if not application.was_rejected:
            raise Exception("Wait for your application's accept/reject")
        elif get_days_delta(application.reject_date) < 4:
            raise Exception("Your applicated recently")
        application.reject_date = None
        application.was_rejected = False
        application.save()
    except Application.DoesNotExist:
        Application.objects.create(user=request.user, room_id=room_id)
    return redirect('show_room', room_id=room_id)





@login_required
@only_for_author
def manage_applications(request, room_id):
    applications = Application.objects.filter(room=room_id, was_rejected=False).select_related()
    if request.method == 'POST':
        for a in request.POST.keys():
            if request.POST[a] == 'A':
                Membership.objects.create(room_id=room_id, user_id=int(a))
            else:
                applications.update(was_rejected=True, reject_date=datetime.now())
    else:
        pass
    return render(request, template_name='chat/manage_applications.html', context={'applications': applications, 'rid': room_id, 'title': "Room's applications"})
