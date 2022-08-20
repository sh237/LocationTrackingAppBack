from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CreateLocationViewSet

app_name = 'api'
router = DefaultRouter()

# api/todo/
router.register('', CreateLocationViewSet)

urlpatterns = [
    path('', include(router.urls), name='crud'),
    path('create/', CreateLocationViewSet.as_view(),name='create')
]