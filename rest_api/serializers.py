from rest_framework import serializers
from mainapp.models import Rooms
from authsys.models import CustomUser
from rest_framework.validators import ValidationError



class RoomSerializer(serializers.ModelSerializer):

    def validate_room_name(self, value):
        if value.lower().__contains__('maga'):
            raise ValidationError('Very funny, remove my name from room name')
        return value

    def create(self, validated_data):
        core_data = {'author': self.context['request'].user}
        return Rooms.objects.create(**validated_data, **core_data)




    class Meta:
        model = Rooms
        fields = '__all__'
        read_only_fields = ['rated_persons',
                            'members',
                            'author',
                            'create_date',
                            'update_date']
