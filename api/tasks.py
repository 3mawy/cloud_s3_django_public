from botocore.exceptions import ClientError
from celery import shared_task

from api.views.helper import boto3_s3_resource_connect


@shared_task
def fetch_objects_metadata(serialized_credentials):

    try:
        s3 = boto3_s3_resource_connect(serialized_credentials)
        objects_metadata = {}
        total_size = 0
        total_count = 0
        for bucket in s3.buckets.all():
            bucket_name = bucket.name
            size = 0
            count = 0
            for obj in bucket.objects.all():
                count += 1
                size += obj.size

            objects_metadata[bucket_name] = {
                'size': "%.3f GB" % (size * 1.0 / 1024 / 1024 / 1024),
                'count': count
            }

            total_count += count
            total_size += size

        objects_metadata['overall_total'] = {
            'total_size': "%.3f GB" % (total_size * 1.0 / 1024 / 1024 / 1024),
            'total_count': total_count
        }
        return objects_metadata
    except ClientError as e:
        raise Exception(str(e))
