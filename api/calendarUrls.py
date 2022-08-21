from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CreateCalendarViewSet,CalendarViewSet

app_name = 'calendar'
router = DefaultRouter()

# api/location/
router.register('', CalendarViewSet)
# router.register('create/', CreateLocationViewSet)

urlpatterns = [
    path('', include(router.urls), name='crud'),
    path('create/', CreateCalendarViewSet.as_view(),name='create')
]