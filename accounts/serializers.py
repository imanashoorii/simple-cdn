import re

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'}, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name', 'last_name', 'email',
                  'password', 'password_confirm', 'last_login', 'date_joined']

        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data.get('password') != data.get('password_confirm'):
            raise serializers.ValidationError('Passwords do not match')
        return data

    def validate_username(self, username):
        pattern = r"^[A-Za-z]+(?:[_-]*[A-Za-z0-9]+)*$"
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=username).exists():
            raise serializers.ValidationError("Duplicate username.")
        if not re.match(pattern, username) or "admin" in username:
            raise serializers.ValidationError("Username is not valid.")
        return username

    def validate_email(self, email):
        pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=email).exists():
            raise serializers.ValidationError("Duplicate email.")
        if not re.match(pattern, email):
            raise serializers.ValidationError("Email address is not valid.")
        return email

    def create(self, validated_data):
        validated_data.pop('password_confirm', None)
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if '@' not in attrs.get(self.username_field) or not re.match(email_pattern, attrs.get(self.username_field)):
            raise exceptions.ParseError(
                "Email not entered correctly"
            )
        return super().validate(attrs)
