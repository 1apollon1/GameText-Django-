from django import template

register = template.Library()

@register.filter()
def is_member(req, room):
    if req.user in room.members.all():
        if req.user.membership_set.get(room=room).can_write:
            return "MnotW"
        else:
            return "MW"
    else:
        return "notMnotW"

@register.inclusion_tag('chat/show_manage_tools.html')
def show_manage_tools(room_id):
    return {'rid': room_id}
