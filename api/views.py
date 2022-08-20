from rest_framework import generics
from .serializers import LocationSeriarizer

class CreateLocationViewSet(generics.CreateAPIView):
    serializer_class = LocationSeriarizer