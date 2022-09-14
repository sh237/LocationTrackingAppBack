from django.urls import path,include
from .views import UserViewSet,ManageUserView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('myself', ManageUserView.as_view(), name='myself'),
    path('',include(router.urls)),
]