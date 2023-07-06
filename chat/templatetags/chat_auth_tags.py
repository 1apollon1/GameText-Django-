from django import template

register = template.Library()

@register.filter()
def can_write(req, room):
    if req.user in room.members.all() and req.user.membership_set.get(room=room).can_write:
        return True
    else:
        return False

@register.inclusion_tag('chat/show_manage_tools.html')
def show_manage_tools(room_id):
    return {'rid': room_id}
