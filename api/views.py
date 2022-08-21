from rest_framework import generics
from .serializers import LocationSeriarizer, CalendarSeriarizer
from .models import Location
from rest_framework import viewsets

class CreateLocationViewSet(generics.CreateAPIView):
    serializer_class = LocationSeriarizer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSeriarizer

class CreateCalendarViewSet(generics.CreateAPIView):
    serializer_class = CalendarSeriarizer

class CalendarViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = CalendarSeriarizer