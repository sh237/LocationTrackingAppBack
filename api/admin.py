from django.contrib import admin                                                                                                         
from django.contrib.gis import admin as geoadmin                                                                                         
from . import models
admin.site.register(models.Location, geoadmin.OSMGeoAdmin)
# admin.site.register(models.Location)
admin.site.register(models.Calendar)
admin.site.register(models.Photo)