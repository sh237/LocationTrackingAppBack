from rest_framework import serializers
from api.models import Location, Calendar


class LocationSeriarizer(serializers.ModelSerializer):

    created = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)
    # updated = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)

    class Meta:
        model = Location
        fields = ['calendar', 'location',  'speed']

        extra_kwargs = {'calendar': {'write_only': True}}