from rest_framework import serializers, validators

from api.models import AWSCredentials
from django.core.exceptions import ValidationError


def validate_url_safe(value):
    if not value.isascii() or not value.replace('-', '').replace('_', '').isalnum():
        raise ValidationError(
            'The identifier must only contain letters, numbers, hyphens, and underscores.',
            params={'value': value},
        )


class AWSCredentialsSerializer(serializers.ModelSerializer):
    identifier = serializers.CharField(
        max_length=100,
        min_length=3,
        validators=[validators.UniqueValidator(queryset=AWSCredentials.objects.all()), validate_url_safe],
    )

    class Meta:
        model = AWSCredentials
        fields = ['identifier', 'aws_access_key_id', 'aws_secret_access_key', 'region_name']
        required = True
