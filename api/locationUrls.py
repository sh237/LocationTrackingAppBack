from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CreateLocationViewSet,LocationViewSet

app_name = 'location'
router = DefaultRouter()


# api/location/
router.register('', LocationViewSet)
# router.register('create/', CreateLocationViewSet)

urlpatterns = [
    path('', include(router.urls), name='crud'),
    path('create/', CreateLocationViewSet.as_view(),name='create')
]