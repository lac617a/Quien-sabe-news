from storages.backends.s3boto3 import S3Boto3Storage
class StaticStorage(S3Boto3Storage):
    bucket_name = 'qsn-s3'
    location = 'static'
    default_acl = 'private'

class MediaStorage(S3Boto3Storage):
    bucket_name = 'qsn-s3'
    location = 'media'
    default_acl = 'private'
    file_overwrite = False