from decouple import config

DATABASES_ENV={
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':config('DB_NAME'),
        'USER':config('DB_USER'),
        'PASSWORD':config('DB_PASS'),
        'HOST':config('DB_HOST'),
        'PORT':'5432',
    }
}
DATABASES_DEV={
  'default':{
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME':'news',
    'USER':'postgres',
    'PASSWORD':config('DB_PASS'),
    'HOST':'localhost',
    'PORT':'5432',
  }
}