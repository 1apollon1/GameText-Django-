from django import template

register = template.Library()

@register.filter()
def is_member(req, room):
    if req.user in room.members.all():
        return True
    else:
        return False
