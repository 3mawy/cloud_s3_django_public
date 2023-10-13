from rest_framework.response import Response
from rest_framework import status
import boto3


def get_credentials_from_param(request):
    user = request.user
    aws_cred = request.GET.get('aws_cred')
    if aws_cred:
        user_credentials = user.awscredentials_set.get(identifier=aws_cred)
    else:
        user_credentials = user.awscredentials_set.first()
    if user_credentials is None:
        return Response({'error': 'No credentials available'}, status=status.HTTP_404_NOT_FOUND)
    return user_credentials


def boto3_s3_client_connect(user_credentials):
    return boto3.client('s3',
                        aws_access_key_id=user_credentials.aws_access_key_id,
                        aws_secret_access_key=user_credentials.aws_secret_access_key,
                        region_name=user_credentials.region_name)


def boto3_s3_resource_connect(user_credentials):
    return boto3.resource('s3',
                          aws_access_key_id=user_credentials["aws_access_key_id"],
                          aws_secret_access_key=user_credentials["aws_secret_access_key"],
                          region_name=user_credentials["region_name"])


def get_file_acl(bucket_name, file_key):
    s3 = boto3.client('s3')
    response = s3.get_object_acl(Bucket=bucket_name, Key=file_key)
    return response['Grants']
