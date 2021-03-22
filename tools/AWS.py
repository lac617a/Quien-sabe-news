from decouple import config

# AWS S3
USE_S3 = True #config('USE_S3',default=False,cast=bool)
AWS_ACCESS_KEY_ID = config('AWS_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_KEY')
AWS_STORAGE_BUCKET_NAME = 'qsn-s3'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400',}
AWS_S3_SECURE_URLS = True
AWS_DEFAULT_ACL = 'plublic-read'
AWS_QUERYSTRING_AUTH = False
