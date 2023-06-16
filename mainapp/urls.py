from django.urls import path




from .views import *
urlpatterns = [
    path('', Main.as_view(), name='get_to_main'),
    path('room/<int:roomid>', ShowRoom.as_view(), name='show_room'),
    path('users/<int:userid>', show_user, name='show_user'),
    path('create', CreateRoomView.as_view(), name='create_room')
]
