from bms.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bms_db',
        'USER': 'postgres',
        'PASSWORD': 'asdfg123',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

# CELERY
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
