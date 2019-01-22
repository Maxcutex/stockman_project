from allauth.account.adapter import get_adapter
from allauth.account.forms import ResetPasswordForm
from allauth.account.utils import setup_user_email
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import PasswordResetSerializer
from rest_framework import serializers

from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'email',
                  'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Create and return new user. """

        user = UserProfile(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_active=True
        )

        user.set_password(validated_data['password'])
        user.save()

        return user



class PasswordSerializer (PasswordResetSerializer):
    password_reset_form_class = ResetPasswordForm

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'password1', 'password2' )
        extra_kwargs = {'password1': {'write_only': True}, 'password2': {'write_only': True} }

    def create(self, validated_data):
        user = UserProfile.objects.create_user(validated_data['email'],
                                        None,
                                        validated_data['password1'])
        return user


class RegisterSerializerCustom(RegisterSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = UserProfile
        fields = '__all__'

    def get_cleaned_data(self):
        return {
        'password1': self.validated_data.get('password1', ''),
        'password2': self.validated_data.get('password2', ''),
        'email': self.validated_data.get('email', ''),
        'first_name': self.validated_data.get('first_name', ''),
        'last_name': self.validated_data.get('last_name', ''),
    }

    def validate_email(self, email):
        pattern = r"^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$"
        if len(email) > 7  and bool(re.match(pattern, email)):
            return email
        raise serializers.ValidationError('Invalid email address')

    def validate_password1(self, password1):
        pattern = r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,60}$"
        if bool(re.match(pattern, password1)):
            return password1
        raise serializers.ValidationError('password must be atleast 6 characters, must include numbers, chararcers, uppercase and lowercase character')

    def validate_password2(self, password2):
        password1 = self.initial_data.get('password1', None)
        if password1 == password2:
            return password2
        raise serializers.ValidationError('Passwords did not match.')


    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.first_name = self.cleaned_data['first_name']
        user.last_name  = self.cleaned_data['last_name']
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user
