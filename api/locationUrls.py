from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet,LocationUpdateAPIView

app_name = 'location'
router = DefaultRouter()


# api/location/
router.register('', LocationViewSet)
# router.register('create/', CreateLocationViewSet)

urlpatterns = [
    path('', include(router.urls), name='crud'),
    path('update/<int:calendar__id>', LocationUpdateAPIView.as_view(), name='update_location'),
    # path('create/', CreateLocationViewSet.as_view(),name='create_location'),
]