from django import template
from mainapp.models import *
import datetime

register = template.Library()


@register.filter()
def get_type(room_name):
    return f'{room_name} <-----> {Rooms.objects.get(room_name=room_name).type.type_name}'


@register.simple_tag
def get_room(id):
    return Rooms.objects.get(pk=id)


@register.inclusion_tag('mainapp/list_types.html')
def show_types():
    return {'types': RoomType.objects.all()}

@register.inclusion_tag('mainapp/list_pagination_content.html')
def show_pag(pag, req, selpage):
    def_dict = {'paginator': pag, 'selected_page': selpage}
    for key in req.GET.keys():
        def_dict[key] = req.GET[key]

    return def_dict





