from django.urls import path
from .views import *

urlpatterns = [
    path('rooms/', PrimitiveApi.as_view())

]