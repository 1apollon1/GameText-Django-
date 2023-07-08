from mainapp.models import Membership

def get_change_dict(request):
    change_dict = {}
    for key in request.POST.keys():
        try:
            member, attr = tuple(key.split('|'))
            member = int(member)
        except ValueError:
            continue
        if member not in change_dict.keys():
            if request.user.pk == member:
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
            Membership.objects.get(pk=memid).delete()
            continue
        Membership.objects.filter(id=memid).update(**change_dict[memid])
