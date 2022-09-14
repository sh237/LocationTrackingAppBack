from rest_framework import serializers
from api.models import Location, Calendar


class LocationSeriarizer(serializers.ModelSerializer):

    created = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)
    # updated = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)

    class Meta:
        model = Location
        fields = ['calendar', 'location','created']

        extra_kwargs = {'calendar': {'write_only': True}}

class CalendarSeriarizer(serializers.ModelSerializer):

    created = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)
    # updated = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)

    class Meta:
        model = Calendar
        fields = ['user', 'date','created']

        extra_kwargs = {'user': {'write_only': True},'date': {'write_only': True}}