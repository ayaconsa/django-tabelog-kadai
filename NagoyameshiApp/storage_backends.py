import os
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'
    bucket_name = os.environ['AWS_STORAGE_BUCKET_NAME_STATIC']

class MediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    bucket_name = os.environ['AWS_STORAGE_BUCKET_NAME_MEDIA']
