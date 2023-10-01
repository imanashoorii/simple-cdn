import re

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', "first_name", "last_name", 'email',
                  'password', "updated_at", "created_at", "last_login", "date_joined"]

        extra_kwargs = {'password': {'write_only': True}}

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
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

