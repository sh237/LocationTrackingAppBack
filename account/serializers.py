from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'username', 'password']
        extra_kwargs = {'password':{'write_only':True, 'required':True}}

    def create(self, validated_data):
        # print("Validated data",validated_data)
        user = User.objects.create_user(**validated_data)
        # Token.objects.create(user=user)
        return user


# class CreateUserSerializer(serializers.ModelSerializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True,
#                                      style={'input_type': 'password'})

#     class Meta:
#         model = User
#         fields = ('email','username', 'password', 'first_name',)
#         write_only_fields = ('password')
#         read_only_fields = ('is_staff', 'is_superuser', 'is_active',)

#     def create(self, validated_data):
#         user = super(CreateUserSerializer, self).create(validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
