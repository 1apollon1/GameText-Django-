from django.contrib import admin
from .models import *

from django.contrib import admin

admin.site.site_header = "Text Game Admin"

@admin.display(description="Here is name of rooms'author")
def upper_case_author_name(obj):
    return obj.room_author_name.upper()



class MainappAdmin(admin.ModelAdmin):
    list_display_links = ['room_name']
    list_editable = []
    list_display = ['room_name', upper_case_author_name, 'type', 'create_date']
    search_fields = ['room_name', 'room_author_name']
    search_help_text = 'Enter search query'
    show_full_result_count = False

admin.site.register(Rooms, MainappAdmin)


# Register your models here.
