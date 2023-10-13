from botocore.exceptions import ClientError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status

from api.views.helper import get_credentials_from_param, boto3_s3_client_connect


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_buckets(request):
    user_credentials = get_credentials_from_param(request)
    try:
        s3 = boto3_s3_client_connect(user_credentials)
        buckets = s3.list_buckets()

        buckets_with_grants = []

        for bucket in buckets['Buckets']:
            bucket_name = bucket['Name']

            acl = s3.get_bucket_acl(Bucket=bucket_name)

            bucket_info = {
                'bucket_name': bucket_name,
                'grants': acl['Grants']
            }

            buckets_with_grants.append(bucket_info)
        return Response(buckets_with_grants, status=status.HTTP_200_OK)

    except ClientError as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_bucket_permissions(request, bucket_name):
    user_credentials = get_credentials_from_param(request)
    try:
        s3 = boto3_s3_client_connect(user_credentials)
        response = s3.get_bucket_acl(Bucket=bucket_name)
        return Response(response, status=status.HTTP_200_OK)

    except ClientError as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)


# TODO: Refactor
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_bucket_paginated_objects(request, bucket_name):
    user_credentials = get_credentials_from_param(request)
    prefix = request.query_params.get('prefix', '')  # Get the prefix from query parameters
    next_marker = request.query_params.get('next_marker', '')  # Get the marker from query parameters for pagination

    try:
        s3 = boto3_s3_client_connect(user_credentials)
        paginator = s3.get_paginator('list_objects')

        operation_parameters = {
            'Bucket': bucket_name,
            'Prefix': prefix,
            'Delimiter': '/',
            'MaxKeys': 12,
            'Marker': next_marker
        }
        page_iterator = paginator.paginate(**operation_parameters)
        for page in page_iterator:
            files = page.get('Contents', [])
            folders = [obj['Prefix'] for obj in page.get('CommonPrefixes', [])]
            marker = page.get('Marker', '')
            next_marker = page.get('NextMarker', '')
            result = {'folders': folders, 'files': [], 'marker': marker, 'next_marker': next_marker}
            for file_obj in files:
                file_key = file_obj['Key']
                file_acl_response = s3.get_object_acl(Bucket=bucket_name, Key=file_key)
                file_permissions = file_acl_response['Grants']
                result['files'].append({'file': file_key, 'grants': file_permissions})

            return Response(result, status=status.HTTP_200_OK)
    except ClientError as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
