from rest_framework import serializers
from api.models import Location, Calendar
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class LocationSeriarizer(GeoFeatureModelSerializer):

    # created_at = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)
    # updated = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)

    class Meta:
        model = Location
        fields = ['id','calendar', 'mpoint']
        geo_field = 'mpoint'
        auto_bbox = False

    # def create(self, validated_data):
    #     return Location.objects.create(**validated_data)
    def update(self, instance, validated_data):
        print("validated_data",validated_data)
        print("instance",instance)
        instance.calendar = validated_data["calendar"]
        instance.mpoint = validated_data["mpoint"] + instance.mpoint
        instance.save()
        return instance


class CalendarSeriarizer(serializers.ModelSerializer):

    created = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)
    # updated = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)

    class Meta:
        model = Calendar
        fields = ['id', 'user', 'date','created', 'title', 'description']

        # extra_kwargs = {'user': {'write_only': True},'date': {'write_only': True}}
        def update(self, instance, validated_data):
            print("instance",instance)
            instance.save()
            return instance

