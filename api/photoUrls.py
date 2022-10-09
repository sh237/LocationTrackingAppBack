from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import LocationExitViewSet, LocationViewSet,LocationUpdateAPIView, PhotoViewSet

app_name = 'photo'
router = DefaultRouter()


# api/location/
router.register('', PhotoViewSet)
# router.register('create/', CreateLocationViewSet)

urlpatterns = [
    path('', include(router.urls), name='crud'),
]