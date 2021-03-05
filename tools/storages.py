from storages.backends.s3boto3 import S3Boto3Storage
class MediaStorage(S3Boto3Storage):
    bucket_name = 'static_qsn'
    location = 'media'
    file_overwrite = False

class StaticStorage(S3Boto3Storage):
    bucket_name = 'static_qsn'
    location = 'static'
    file_overwrite = False