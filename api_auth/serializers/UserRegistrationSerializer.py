from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=100,
        min_length=6,
        validators=[UniqueValidator(queryset=User.objects.all())],
        required=True
    )
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
