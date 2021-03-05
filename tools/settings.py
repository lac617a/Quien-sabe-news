"""
Django settings for tools project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from typing import cast
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG',default=True,cast=bool)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # sitemap
    'django.contrib.sites',
    'django.contrib.sitemaps',
    # bitly
    'django_bitly',
    # DRF
    'rest_framework',
    # App
    'news',
    'categories',
    'ckeditor',
    'hitcount',
    'storages',
]

SITE_ID = 1 # new

CKEDITOR_CONFIGS = {
    'default': {
        'height':'500px',
        # tab key conversion space number
        'tabSpaces': 2,
        # Toolbar Style
        'toolbar': None,
        # Toolbar buttons
        'toolbar_Custom': [
            ['Format'],
            ['Smiley', 'CodeSnippet'],
            ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
            ['TextColor', 'BGColor'],
            ['Link', 'Unlink'],
            ['NumberedList', 'BulletedList'],
            ['Maximize'],
            ['Image','imageTextAlternative'],
        ],
        # Add Code Block Plug-ins
        'extraPlugins': ','.join(['codesnippet']),
        'codeSnippet_languages': {
            'bash': 'Bash',
            'css': 'CSS',
            'django': 'Django',
            'html': 'HTML',
            'javascript': 'JavaScript',
            'php': 'PHP',
            'python': 'Python',
        }
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'tools.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tools.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES={
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':config('DB_NAME'),
        'USER':config('DB_USER'),
        'PASSWORD':config('DB_PASS'),
        'HOST':config('DB_HOST'),
        'PORT':'5432',
    }
}

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = False



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# COLLECTSTATIC
# AWS S3
# if USE_S3:
USE_S3 = config('USE_S3',default=False,cast=bool)
AWS_ACCESS_KEY_ID = config('AWS_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_KEY')
AWS_STORAGE_BUCKET_NAME = 'qsn-s3'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400',}
AWS_S3_SECURE_URLS = True
AWS_DEFAULT_ACL = 'plublic-read'

# AWS_LOCATION = 'static'
# STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]

# DEFAULT_FILE_STORAGE  =  'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN,AWS_LOCATION)

AWS_QUERYSTRING_AUTH = False

# s3 public media settings
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'tools.storages.MediaStorage'

# carga de de static
PUBLIC_STATIC_LOCATION ='static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_STATIC_LOCATION}/'
STATICFILES_DIRS = (os.path.join(BASE_DIR,"static" ),)
STATICFILES_STORAGE = 'tools.storages.StaticStorage'

if DEBUG:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
    # WhiteNoise
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# HitCount
SESSION_SAVE_EVERY_REQUEST = True
CSRF_COOKIE_SECURE = True
# HITCOUNT_KEEP_HIT_ACTIVE = {'minutes': 60}
# HITCOUNT_HITS_PER_IP_LIMIT = 0  # unlimited
# HITCOUNT_KEEP_HIT_IN_DATABASE = {'seconds': 10}

CKEDITOR_UPLOAD_PATH = "CkEditor/"

# BITLY
BITLY_LOGIN = 'botlacrita617@gmail.com'
BITLY_API_KEY = 'e54ed519ec2761d8a93f10f791a84c5cc555681c'