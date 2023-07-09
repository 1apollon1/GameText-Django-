from django.urls import path

from . import views

urlpatterns = [
    path("room/<int:room_id>", views.room, name="show_room"),
    path('manage/<int:room_id>/options', views.ManageRoomOptions.as_view(), name='manage_room_options'),
    path('manage/<int:room_id>/members', views.manage_room_members, name='manage_room_members'),
    path('room/applicate/<int:room_id>', views.application_send, name='applicate'),
    path('room/<int:room_id>/applications', views.manage_applications, name='manage_room_applications')
]