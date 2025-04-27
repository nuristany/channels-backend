import os
from .common import *
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABSE_PORT')
    }
}

CSRF_TRUSTED_ORIGINS = [
    "https://channels-backend-production.up.railway.app",
    "https://your-frontend-domain.com"
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://your-frontend-domain.com"
]


CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SAMESITE = 'Lax'
