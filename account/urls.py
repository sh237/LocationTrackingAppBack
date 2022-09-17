from django.urls import path,include
from .views import UserViewSet,ManageUserView
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUserAPIView,LogoutUserAPIView

router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('login',obtain_auth_token, name='auth_user_login'),
    path('register',CreateUserAPIView.as_view(), name='auth_user_create'),
    path('logout', LogoutUserAPIView.as_view(), name='auth_user_logout'),
    path('',include(router.urls)),
]