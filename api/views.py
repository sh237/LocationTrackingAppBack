from rest_framework import generics
from .serializers import LocationSeriarizer, CalendarSeriarizer
from .models import Location
from .models import Calendar
from rest_framework import viewsets
from rest_framework_gis.filters import DistanceToPointFilter
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import  get_object_or_404
from rest_framework.response import Response
from rest_framework import status

# class CreateLocationViewSet(generics.CreateAPIView):
#     serializer_class = LocationSeriarizer
#     authentication_classes = (TokenAuthentication, )
#     permission_classes = (IsAuthenticated, )

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     # We create a token than will be used for future auth
    #     return Response(
    #         {**serializer.data},
    #         status=status.HTTP_201_CREATED,
    #         headers=headers
    #     )

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSeriarizer
    filter_backends = [filters.SearchFilter, DistanceToPointFilter]
    distance_filter_field = 'mpoint'
    search_fields = ['calendar']
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    lookup_field = 'calendar__id'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # We create a token than will be used for future auth
        return Response(
            {**serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )

# class CreateCalendarViewSet(generics.CreateAPIView):
#     serializer_class = CalendarSeriarizer
#     authentication_classes = (TokenAuthentication, )
#     permission_classes = (IsAuthenticated, )

class LocationUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSeriarizer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    lookup_field = 'calendar__id'


class CalendarViewSet(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSeriarizer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=date']
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    lookup_field = 'user__id'
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # We create a token than will be used for future auth
        return Response(
            {**serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )

class MultipleFieldLookupMixin(object):
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj

# class CalendarRetrieveAPIView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
#     queryset = Calendar.objects.all()
#     serializer_class = CalendarSeriarizer
#     filter_backends = [filters.SearchFilter]
#     lookup_fields = ('user_id')
#     search_fields = ['=date']