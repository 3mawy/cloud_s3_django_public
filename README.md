# cloud_s3_django

Cloud S3 is an API for a web application that allows users to easily manage and navigate Amazon S3 buckets and objects. It provides a user-friendly interface for listing, viewing, and interacting with files stored in Amazon S3.

## Features

- List all S3 buckets associated with a user's account.
- Display the contents of selected buckets, including files and folders.
- View details about individual objects, such as metadata and access permissions.
- Secure user authentication to ensure data privacy.
- Secure user authentication to ensure data privacy.
- User can have multiple sets of AWS credentials encrypted securely in the database.
- Easily switch between different AWS accounts and their associated buckets.

## Installation and Setup
```
docker-compose up 
```


# Project: API REFERENCE AWS S3 PANEL
# 📁 Collection: Auth 


## End-point: register
### Method: POST
>```
>http://localhost:8004/api/register
>```
### Body (**raw**)

```json
{
    "username": "userName",
    "password":"password"
}
```


### Response: 201
```json
{
    "message": "Registered successfully"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: login
### Method: POST
>```
>http://localhost:8004/api/login
>```
### Body (**raw**)

```json
{
    "username": "userName",
    "password":"password"
}
```

### Response: 200
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MzM2NzkzOCwiaWF0IjoxNjkzMjgxNTM4LCJqdGkiOiJjY2QyMzA1ZGMyZjA0ZTZhYmQ5ODQ4NjJjZWQ4ZTY5OCIsInVzZXJfaWQiOjMyfQ.hMhRlvwc6f6UrTD4i899CF3Qfdh3qJt5RueQ2zrKKck",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkzNTgxNTM4LCJpYXQiOjE2OTMyODE1MzgsImp0aSI6ImJhNTE1NDZiODdhZTQwZjNhNWZiZGMzMTFkMGFjYmFhIiwidXNlcl9pZCI6MzJ9.PYv1rIO8EV5lkKUgG4b60UdRx84sH7Df_NI3Hb7xOyE"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: refresh token
### Method: POST
>```
>http://localhost:8004/api/token/refresh
>```
### Body (**raw**)

```json
{"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MzM2NzkzOCwiaWF0IjoxNjkzMjgxNTM4LCJqdGkiOiJjY2QyMzA1ZGMyZjA0ZTZhYmQ5ODQ4NjJjZWQ4ZTY5OCIsInVzZXJfaWQiOjMyfQ.hMhRlvwc6f6UrTD4i899CF3Qfdh3qJt5RueQ2zrKKck"}
```


### Response: 200
```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkzNTgxNTczLCJpYXQiOjE2OTMyODE1MzgsImp0aSI6IjE0MjM4NjIzMjcyZTQ3Nzc4MDE0NmVjZjA1MGQ0MzliIiwidXNlcl9pZCI6MzJ9.rDJI7SkhddpUsjdbRrujOHTXJoBeI7vX-mzMirfvWJI",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MzM2Nzk3MywiaWF0IjoxNjkzMjgxNTczLCJqdGkiOiI4ZmI4OWUxM2VkNWE0ZDZkYmViMTcwOTc2ODhiNzVmYSIsInVzZXJfaWQiOjMyfQ.IscvNcjy53nGskEE0rdt0I0Z_Af12rGoNDk-WpsI7qo"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: get all buckets
### Method: GET
>```
>http://localhost:8004/api/buckets/?aws_cred=romiles
>```
### Query Params

|Param|value|
|---|---|
|aws_cred|romiles|


### Response: 200
```json
[
    {
        "bucket_name": "romiles-s3",
        "grants": [
            {
                "Grantee": {
                    "ID": "8e3a815c82c741fd12fa6aebc16a2176798c95b1de97ba94dddd72e982538949",
                    "Type": "CanonicalUser"
                },
                "Permission": "FULL_CONTROL"
            }
        ]
    }
]
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃


## End-point: get bucket folders
### Method: GET
>```
>http://localhost:8004/api/buckets/romiles-s3/folders/?aws_cred=romiles&prefix=media/&next_marker=media/
>```
### Query Params

|Param|value|
|---|---|
|aws_cred|romiles|
|prefix|media/|
|next_marker|media/|


### Response: 200
```json
{
    "folders": [
        "media/.template-manager/",
        "media/.thumbswysiwyg/",
        "media/analytics/"
    ],
    "files": [
        {
            "file": "media/.template-managerfootertranslated64def753ba6f9-thumb.jpg",
            "grants": [
                {
                    "Grantee": {
                        "ID": "8e3a815c82c741fd12fa6aebc16a2176798c95b1de97ba94dddd72e982538949",
                        "Type": "CanonicalUser"
                    },
                    "Permission": "FULL_CONTROL"
                }
            ]
        },
        {
            "file": "media/.template-managerfootertranslated64def753ba6f9.jpg",
            "grants": [
                {
                    "Grantee": {
                        "ID": "8e3a815c82c741fd12fa6aebc16a2176798c95b1de97ba94dddd72e982538949",
                        "Type": "CanonicalUser"
                    },
                    "Permission": "FULL_CONTROL"
                }
            ]
        },
        {
            "file": "media/.template-managerorientdescription648ae75e73cf5-thumb.jpg",
            "grants": [
                {
                    "Grantee": {
                        "ID": "8e3a815c82c741fd12fa6aebc16a2176798c95b1de97ba94dddd72e982538949",
                        "Type": "CanonicalUser"
                    },
                    "Permission": "FULL_CONTROL"
                }
            ]
        }
    ],
    "marker": "media/",
    "next_marker": "media/catalog/"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃


## End-point: get current user AWS credentials
### Method: GET
>```
>http://localhost:8004/api/aws-credentials
>```
### Response: 200
```json
[
  
    {
        "identifier": "romiles",
        "aws_access_key_id": "AKIA************PLXX",
        "aws_secret_access_key": "EOfK********************************9Efk",
        "region_name": "us-east-1"
    },
    {
        "identifier": "ideaaaaaaaaantifier",
        "aws_access_key_id": "ASIA************PNXX",
        "aws_secret_access_key": "ESfX********************************9Efk",
        "region_name": "us-east-2"
    }
]
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: add AWS credentials
### Method: POST
>```
>http://localhost:8004/api/aws-credentials/add
>```
### Body (**raw**)

```json
{
        "identifier":"ideaaaaaaaaaantaaiasassfier",
        "aws_access_key_id":"ASIA************PNXX",
                "aws_secret_access_key": "ESfX********************************9Efk",
                    "region_name":"us-east-2"

}
```

### Response: 201
```json
{
    "identifier": "ideaaaaaaaaaantaaiasassfier",
    "aws_access_key_id": "ASIA************PNXX",
    "aws_secret_access_key": "ESfX********************************9Efk",
    "region_name": "us-east-2"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: get object link
### Method: POST
>```
>http://localhost:8004/api/buckets/romiles-s3/objects/get_presigned_url?aws_cred=romiles
>```
### Body (**raw**)

```json
{
    "object_key":"media/LICENSE.txt"
}

```

### Query Params

|Param|value|
|---|---|
|aws_cred|romiles|


### Response: 200
```json
{
    "presigned_url": "https://romiles-s3.s3.amazonaws.com/media/LICENSE.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVFSTZBYXY6NLPLXX%2F20230829%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20230829T040436Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=0d9838c547f5de30a8ce7c98211d7a32a80924721d10dcfb169a2c89aea7bdc0"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
## End-point: get object permissions
### Method: GET
>```
>http://localhost:8004/api/buckets/romiles-s3/objects/bWVkaWEvLnRlbXBsYXRlLW1hbmFnZXJvcmllbnRkZXNjcmlwdGlvbjY0OGFlNzVlNzNjZjUtdGh1bWIuanBn=/permissions/?aws_cred=romiles
>```
### Query Params

|Param|value|
|---|---|
|aws_cred|romiles|


### Response: 200
```json
{
    "object permissions": {
        "ResponseMetadata": {
            "RequestId": "0XGFSTJNP8689Y2M",
            "HostId": "NoiVb7eENBu1eT32J3MV8/BSxaUcF0rCKlEbopedl8b40y5S7DBIxImO42KbH+1es3oH8S/HJqQ=",
            "HTTPStatusCode": 200,
            "HTTPHeaders": {
                "x-amz-id-2": "NoiVb7eENBu1eT32J3MV8/BSxaUcF0rCKlEbopedl8b40y5S7DBIxImO42KbH+1es3oH8S/HJqQ=",
                "x-amz-request-id": "0XGFSTJNP8689Y2M",
                "date": "Wed, 23 Aug 2023 03:33:51 GMT",
                "content-type": "application/xml",
                "transfer-encoding": "chunked",
                "server": "AmazonS3"
            },
            "RetryAttempts": 0
        },
        "Owner": {
            "ID": "8e3a815c82c741fd12fa6aebc16a2176798c95b1de97ba94dddd72e982538949"
        },
        "Grants": [
            {
                "Grantee": {
                    "ID": "8e3a815c82c741fd12fa6aebc16a2176798c95b1de97ba94dddd72e982538949",
                    "Type": "CanonicalUser"
                },
                "Permission": "FULL_CONTROL"
            }
        ]
    }
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
## End-point: get bucket details
### Method: GET
>```
>http://localhost:8004/api/buckets/romiles-s3/?aws_cred=romiles
>```
### Query Params

|Param|value|
|---|---|
|aws_cred|romiles|


### Response: 200
```json
{
    "ResponseMetadata": {
        "RequestId": "00QQR80SVHMMXWJC",
        "HostId": "qYTHT+wMPQU86vN2wBydU1Mu3IXWJPes/JsKFqDnZpTByrVioGh+pWlXI2ACYUjmfsjZBK8Vxk4=",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amz-id-2": "qYTHT+wMPQU86vN2wBydU1Mu3IXWJPes/JsKFqDnZpTByrVioGh+pWlXI2ACYUjmfsjZBK8Vxk4=",
            "x-amz-request-id": "00QQR80SVHMMXWJC",
            "date": "Wed, 23 Aug 2023 00:34:44 GMT",
            "content-type": "application/xml",
            "transfer-encoding": "chunked",
            "server": "AmazonS3"
        },
        "RetryAttempts": 0
    },
    "Owner": {
        "ID": "8e3a815c82c741fd12fa6aebc16a2176798c95b1de97ba94dddd72e982538949"
    },
    "Grants": [
        {
            "Grantee": {
                "ID": "8e3a815c82c741fd12fa6aebc16a2176798c95b1de97ba94dddd72e982538949",
                "Type": "CanonicalUser"
            },
            "Permission": "FULL_CONTROL"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

celery 
```
celery -A cloud_s3 worker --loglevel=info
```
