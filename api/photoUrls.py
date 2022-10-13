from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PhotoListViewSet, PhotoViewSet

app_name = 'photo'
router = DefaultRouter()


# api/location/
router.register('', PhotoViewSet)
# router.register('create/', CreateLocationViewSet)

urlpatterns = [
    path('', include(router.urls), name='crud'),
    path('list/<int:calendar__id>',PhotoListViewSet.as_view() , name='list'),
]