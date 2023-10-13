from django.urls import path, include
from api.views import get_buckets, get_bucket_permissions, get_all_objects, get_object_permissions, \
    get_all_user_credentials, add_credentials, get_bucket_paginated_objects, get_presigned_url, get_objects_metadata
from api.views.ObjectView import check_task_status

urlpatterns = [
    path('buckets/', include([
        path('', get_buckets, name='get_buckets'),
        path('<str:bucket_name>/folders/', get_bucket_paginated_objects, name='get_bucket_paginated_objects'),
        path('<str:bucket_name>/objects/get_presigned_url', get_presigned_url, name='get_presigned_url'),
    ])),
    path('aws-credentials/', include([
        path('', get_all_user_credentials, name='get_all_user_credentials'),
        path('add', add_credentials, name='add_credentials'),
    ])),
    path('objects/metadata', get_objects_metadata, name='get_objects_metadata'),
    path('check_task_status/<str:task_id>/', check_task_status, name='check_task_status'),
]

# path('objects/', get_all_objects, name='get_all_objects'),
# gets all objects of all the buckets linked to current credentials TODO: probably will remove
# path('<str:bucket_name>/objects/<str:encoded_object_key>/permissions/',
#      get_object_permissions, name='get_object_permissions'),
# gets the permissions of an object by name incoded TODO: will remove
# path('buckets/<str:bucket_name>/', get_bucket_permissions, name='get_bucket_permissions'),
# gets the permissions of a bucket by name TODO: will remove