import os
from .AWS import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#carga de de static
PUBLIC_STATIC_LOCATION ='static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_STATIC_LOCATION}/'
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static' ),)
STATICFILES_STORAGE = 'tools.storages.StaticStorage'