from django.urls import path




from .views import *
urlpatterns = [
    path('', Main.as_view(), name='get_to_main'),
    path('users/<int:userid>', show_user, name='show_user'),
    path('create', CreateRoomView.as_view(), name='create_room'),
    path('login', login, name='login')
]
