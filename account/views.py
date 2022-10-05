from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .forms import SetPasswordFormCustom
from api import serializers
from .models import User 
from rest_framework import viewsets
from .serializers import UserSerializer, UserUpdateSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, render
from rest_framework.generics import GenericAPIView
from .serializers import CustomPasswordResetSerializer,PasswordResetConfirmSerializer
from rest_auth.views import PasswordResetConfirmView 

class PasswordResetView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CustomPasswordResetSerializer

    def __init__(self, *args, **kwargs):
        """Prints the name of the class if it is used."""
        print(self.__class__.__name__)
        super().__init__(*args, **kwargs)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Password reset e-mail has been sent.', status=200)
        return Response(serializer.errors, status=400)
        


class UserViewSet(viewsets.ModelViewSet):#api/user/users
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

###########################################################
class ManageUserView(generics.RetrieveUpdateAPIView):#api/user/myself
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        return self.request.user

class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny,]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # We create a token than will be used for future auth
        token = Token.objects.create(user=serializer.instance)
        token_data = {"token": token.key}
        return Response(
            {**serializer.data, **token_data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )

class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    lookup_field = 'id'

class UserThemeUpdateAPIView(APIView):
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def patch(self, request, *args, **kwargs):
        print("partial_update")
        data = request.data
        print(data)
        try:
            user_object = User.objects.get(id=data['id'])
            user_object.theme_color = data['theme_color']
            user_object.save()
        except KeyError:
            pass
        serializer = UserSerializer(user_object)
        return Response(serializer.data)

class UserIsTrackingUpdateAPIView(APIView):
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def patch(self, request, *args, **kwargs):
        print("partial_update")
        data = request.data
        print(data)
        try:
            user_object = User.objects.get(id=data['id'])
            user_object.is_tracking = data['is_tracking']
            user_object.save()
        except KeyError:
            pass
        serializer = UserSerializer(user_object)
        return Response(serializer.data)

class LogoutUserAPIView(APIView):
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication, )
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

def LoadPassWordResetConfirmView(request, uidb64, token):
    # return PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html')(request, uidb64=uidb64, token=token)
    return render(request, 'email/password_reset_confirm.html', {'uidb64': uidb64, 'token': token})

class PasswordResetConfirmView(GenericAPIView):
    """
    Password reset e-mail link is confirmed, therefore
    this resets the user's password.
    Accepts the following POST parameters: token, uid,
        new_password1, new_password2
    Returns the success/fail message.
    """
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = (AllowAny,)
    set_password_form = SetPasswordFormCustom

    def dispatch(self, *args, **kwargs):
        return super(PasswordResetConfirmView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": "Password has been reset with the new password."}
        )