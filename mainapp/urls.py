from django.urls import path




from .views import *
urlpatterns = [
    path('', main, name='get_to_main'),
    path('room/<int:pageid>', showroom, name='show_room'),
    path('users/<int:userid>', show_user, name='show_user'),
    path('create', create_room, name='create_room')
]
