import base64
from botocore.exceptions import ClientError
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from api.views.helper import get_credentials_from_param, boto3_s3_client_connect, boto3_s3_resource_connect
from api.tasks import fetch_objects_metadata
from celery.result import AsyncResult


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_objects_metadata(request):
    user_credentials = get_credentials_from_param(request)
    serialized_credentials = {
        'aws_access_key_id': user_credentials.aws_access_key_id,
        'aws_secret_access_key': user_credentials.aws_secret_access_key,
        'region_name': user_credentials.region_name,
    }

    # Trigger the Celery task asynchronously and pass the serialized credentials as an argument
    task_result = fetch_objects_metadata.delay(serialized_credentials)

    # Return a task ID immediately
    return JsonResponse({'task_id': task_result.id}, status=202)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def check_task_status(request, task_id):
    task = AsyncResult(task_id)

    if task.ready():
        if task.successful():
            result = task.result
            return Response({'status': 'completed', 'result': result}, status=200)
        else:
            return Response({'status': 'failed', 'message': 'Task failed to complete'}, status=500)
    else:
        # Task is still running
        return Response({'status': 'running'}, status=202)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_objects(request):
    user_credentials = get_credentials_from_param(request)
    try:
        s3 = boto3_s3_client_connect(user_credentials)

        buckets = s3.list_buckets()
        all_objects = {}

        for bucket in buckets['Buckets']:
            bucket_name = bucket['Name']
            bucket_objects = s3.list_objects_v2(Bucket=bucket_name)
            if 'Contents' in bucket_objects:
                all_objects[bucket_name] = bucket_objects['Contents']

        return Response({'buckets_and_objects': all_objects}, status=200)
    except ClientError as e:
        return Response({'error': str(e)}, status=500)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_object_permissions(request, bucket_name, encoded_object_key):
    user_credentials = get_credentials_from_param(request)

    try:
        object_key = base64.urlsafe_b64decode(encoded_object_key.encode()).decode()

        s3 = boto3_s3_client_connect(user_credentials)
        response = s3.get_object_acl(Bucket=bucket_name, Key=object_key)

        return Response({'object permissions': response}, status=200)

    except ClientError as e:
        return Response({'error': str(e)}, status=500)


# TODO Complete
@api_view(['POST'])
def get_presigned_url(request, bucket_name):
    user_credentials = get_credentials_from_param(request)
    object_key = request.data['object_key']
    try:
        s3 = boto3_s3_client_connect(user_credentials)
        presigned_url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_key},
            ExpiresIn=3600  # The URL will expire in 1 hour (adjust as needed)
        )
        return Response({'presigned_url': presigned_url})
    except ClientError as e:
        return Response({'error': str(e)}, status=404)
