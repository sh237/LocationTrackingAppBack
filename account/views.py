from tokenize import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import User 
from rest_framework import viewsets
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):#api/user/users
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

class ManageUserView(generics.RetrieveUpdateAPIView):#api/user/myself
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        return self.request.user

###########################################################

class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

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


class LogoutUserAPIView(generics.APIView):
    queryset = User.objects.all()

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
