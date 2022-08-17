from django.db import models

class Calendar(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateField()

class Location(models.Model):
    calendar = models.ForeignKey('Calendar', on_delete=models.CASCADE)
    # location = 