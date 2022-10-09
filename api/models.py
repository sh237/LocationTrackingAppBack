from enum import unique
from django.conf import settings
from django.contrib.gis.db import models
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class Calendar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=39, blank=True,null=True)
    description = models.TextField(blank=True, null=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'date'], name='unique_constraint_calendar')
        ]

class Location(models.Model):
    calendar = models.OneToOneField(Calendar, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    mpoint = models.MultiPointField(blank=True)

class Photo(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    uri = models.CharField(max_length=300,unique=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
