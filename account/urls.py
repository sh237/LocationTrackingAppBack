from django.urls import path,include
from .views import LoadPassWordResetConfirmView, UserThemeUpdateAPIView, UserIsTrackingUpdateAPIView, UserViewSet,ManageUserView
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUserAPIView,LogoutUserAPIView
from .views import PasswordResetView, PasswordResetConfirmView
from .forms import SetPasswordFormCustom

router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('login',obtain_auth_token, name='auth_user_login'),
    path('register',CreateUserAPIView.as_view(), name='auth_user_create'),
    path('logout', LogoutUserAPIView.as_view(), name='auth_user_logout'),
    path('myself', ManageUserView.as_view(), name='auth_user_myself'),
    path('update/theme', UserThemeUpdateAPIView.as_view(), name='auth_user_update'),
    path('update/is_tracking', UserIsTrackingUpdateAPIView.as_view(), name='auth_user_update'),
    path('user',include(router.urls)),
    path('password/reset', PasswordResetView.as_view()),
    path('rest-auth', include('rest_auth.urls')),
    path('reset/<uidb64>/<token>',
        PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('load/<uidb64>/<token>',LoadPassWordResetConfirmView, name='password_reset_load'),
    path('', include('django.contrib.auth.urls')),
    
]