from django.urls import path

from . import views

urlpatterns = [
    path("room/<int:room_id>", views.room, name="show_room"),
    path('manage/<int:room_id>', views.ManageRoomOptions.as_view(), name='manage_room')
]