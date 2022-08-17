from django.conf import settings
from django.contrib.gis.db import models
User = settings.AUTH_USER_MODEL

class Calendar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

class Location(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    location = models.PointField(null=True, blank=True)