from django.urls import path

from .views import *
urlpatterns = [
    path('', main, name='get_to_main'),
    path('rooms/<int:room_page>', showrooms),
]