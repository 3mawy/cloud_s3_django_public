from rest_framework import serializers

from api.models import AWSCredentials


def mask_partially(value):
    prefix = value[:4]
    suffix = value[-4:]
    masked = '*' * (len(value) - 8)
    return f"{prefix}{masked}{suffix}"


class AWSCredentialsHiddenSerializer(serializers.ModelSerializer):
    aws_access_key_id = serializers.SerializerMethodField()
    aws_secret_access_key = serializers.SerializerMethodField()

    class Meta:
        model = AWSCredentials
        fields = ['identifier', 'aws_access_key_id', 'aws_secret_access_key', 'region_name']
        required = True

    def get_aws_access_key_id(self, obj):
        return mask_partially(obj.aws_access_key_id)

    def get_aws_secret_access_key(self, obj):
        return mask_partially(obj.aws_secret_access_key)
