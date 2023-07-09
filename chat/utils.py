from authsys.models import CustomUser
from mainapp.models import *
from datetime import datetime

def get_change_dict(request):
    change_dict = {}
    for key in request.POST.keys():
        try:
            member, attr = tuple(key.split('|'))
            member = int(member)
        except ValueError:
            continue
        if member not in change_dict.keys():
            print(member)
            if request.user == Membership.objects.get(pk=member).user:
                change_dict[member] = {'role': ''}
            else:
                change_dict[member] = {'role': '',
                                       'can_write': False
                                       }
        value = request.POST.get(key)
        if value == 'on':
            value = True
        change_dict[member][attr] = value
    return change_dict

def edit_members(change_dict: dict):
    for memid in change_dict:
        if 'kick' in change_dict[memid]:
            member = Membership.objects.get(pk=memid)
            Application.objects.filter(room_id=member.room_id, user_id=member.user_id).update(was_rejected=True, reject_date=datetime.now())
            member.delete()
            continue
        Membership.objects.filter(id=memid).update(**change_dict[memid])


def get_days_delta(time):
    delta = datetime.now() - time
    return delta.seconds//(3600)






#decorator
def only_for_author(func):
    def wrapper(request, room_id):
        if room_id not in request.user.created_posts.values_list('pk', flat=True):
            raise PermissionError('You are not author of this room')
        return func(request, room_id)
    return wrapper
#decorator



