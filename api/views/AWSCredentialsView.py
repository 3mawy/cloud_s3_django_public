import boto3
from botocore.exceptions import NoCredentialsError
from rest_framework import permissions, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response

from api.serializers import AWSCredentialsSerializer, AWSCredentialsHiddenSerializer
from api.views.helper import boto3_s3_client_connect


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_credentials(request):
    user = request.user
    serializer = AWSCredentialsSerializer(data=request.data)

    if serializer.is_valid():
        user_credentials = serializer.validated_data  # Get the OrderedDict

        try:
            aws_access_key_id = user_credentials['aws_access_key_id']
            aws_secret_access_key = user_credentials['aws_secret_access_key']
            region_name = user_credentials['region_name']

            s3_client = boto3.client('s3',
                                     aws_access_key_id=aws_access_key_id,
                                     aws_secret_access_key=aws_secret_access_key,
                                     region_name=region_name)
            s3_client.list_buckets()  # Test a simple S3 operation

            # Save the credentials to the database only if the test succeeded
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except NoCredentialsError:
            return Response(
                {'error': 'Invalid AWS credentials'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {'error': f'An error occurred: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_user_credentials(request):
    user = request.user
    user_credentials = user.awscredentials_set.all()
    serializer = AWSCredentialsHiddenSerializer(user_credentials, many=True)
    return Response(serializer.data)
