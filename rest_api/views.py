from django.core.exceptions import FieldError
from .permissions import ManageRoomPermission
from rest_framework.response import Response
from .serializers import RoomSerializer
from mainapp.models import Rooms
from rest_framework.viewsets import ModelViewSet
from django.forms.models import model_to_dict


class RoomApiViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    permission_classes = (ManageRoomPermission, )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        request_dict = model_to_dict(instance)
        if len(request_dict) != len(request.data.keys()):
            for field in request.data.keys():
                request_dict[field] = request.data[field]
        serializer = self.get_serializer(instance, data=request_dict, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except FieldError:
            return Response({'failure': 'Invalid GET data'})

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk:
            return Rooms.objects.filter(pk=pk)

        if self.request.method == 'GET':
            return Rooms.objects.filter(**self.request.data)

        return Rooms.objects.all()
