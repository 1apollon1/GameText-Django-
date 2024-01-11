from django.core.exceptions import FieldError
from .permissions import ManageRoomPermission
from rest_framework.response import Response
from .serializers import RatingSerializer
from mainapp.models import Rooms, Rating
from rest_framework.views import APIView
from django.forms.models import model_to_dict


class RatingApiView(APIView):

    def get(self, request):
        try:
            objs = Rating.objects
            if request.data:
                objs = objs.filter(**request.data)
            else:
                objs = objs.all()
            result = RatingSerializer(objs, many=True).data
        except:
            result = 'Invalid data'
        return Response({'result': result})

    def post(self, request):
        resdict = {}
        resdict = request.data | {'echo': 'soccess'}
        return Response(resdict)

