from rest_framework import serializers
from mainapp.models import Rooms
from authsys.models import CustomUser
from rest_framework.validators import ValidationError

class RatingSerializer(serializers.Serializer):
    room_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    is_positive = serializers.BooleanField()
