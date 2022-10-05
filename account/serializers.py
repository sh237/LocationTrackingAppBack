from rest_framework import serializers

from .forms import PasswordResetForm,SetPasswordFormCustom
from account.models import User
from rest_framework.authtoken.models import Token
from rest_auth.serializers import PasswordResetSerializer,PasswordResetConfirmSerializer
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode as uid_decoder
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from rest_framework.exceptions import ValidationError


class CustomPasswordResetSerializer(PasswordResetSerializer):
    password_reset_form_class = PasswordResetForm
    def get_email_options(self):
        data = {
            # 'email_template_name': 'email/password_reset.html',
            'subject_template_name': 'email/password_reset_subject.txt',
            'html_email_template_name': 'email/password_reset.html',
            
        }
        return data

class PasswordResetConfirmSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)
    uid = serializers.CharField()
    token = serializers.CharField()

    set_password_form_class = SetPasswordFormCustom

    def custom_validation(self, attrs):
        pass

    def validate(self, attrs):
        self._errors = {}

        # Decode the uidb64 to uid to get User object
        try:
            uid = force_text(uid_decoder(attrs['uid']))
            self.user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise ValidationError({'uid': ['Invalid value']})

        self.custom_validation(attrs)
        # Construct SetPasswordForm instance
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )
        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)
        if not default_token_generator.check_token(self.user, attrs['token']):
            raise ValidationError({'token': ['Invalid value']})

        return attrs

    def save(self):
        return self.set_password_form.save()

# class PasswordResetConfirmSerializer(PasswordResetConfirmSerializer):
#     password_reset_confirm_form_class=SetPasswordFormCustom
#     form_class = SetPasswordFormCustom
#     set_password_form_class = SetPasswordFormCustom

#     def update(self, instance, validated_data):
#         instance.set_password(validated_data['password'])
#         instance.save()
#         return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'username', 'password', 'theme_color', 'is_tracking']
        extra_kwargs = {'password':{'write_only':True, 'required':True}}

    def create(self, validated_data):
        # print("Validated data",validated_data)
        user = User.objects.create_user(**validated_data)
        # Token.objects.create(user=user)
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'username', 'password', 'theme_color', 'is_tracking']



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