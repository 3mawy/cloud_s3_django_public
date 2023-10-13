from django.db import models
from encrypted_model_fields.fields import EncryptedCharField


class AWSCredentials(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    identifier = models.CharField(max_length=105, unique=True)
    aws_access_key_id = EncryptedCharField(max_length=110)
    aws_secret_access_key = EncryptedCharField(max_length=110)
    region_name = models.CharField(max_length=255)
