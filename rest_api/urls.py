from django.template.defaulttags import url
from django.urls import path, include, re_path
from rest_framework import routers
from .views import RatingApiView

# rooms_router = routers.DefaultRouter()
# rooms_router.register(r'rooms', RoomApiViewSet, basename='rooms')

urlpatterns = [
    path('', RatingApiView.as_view())
    # path('', include(rooms_router.urls)),
    # path('auth/', include('djoser.urls')),
    # path('token/', include('rest_api.authtoken_urls'))

]