from .common import *
from decouple import config

# Secret Key
SECRET_KEY = config('SECRET_KEY', default='insecure-dev-key')

# Always True in development
DEBUG = config('DEBUG', default=True, cast=bool)

# ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.1.106']
ALLOWED_HOSTS = ['*']
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://192.168.1.106:5173',
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:5173',
    'http://192.168.1.106:5173',
]

# SQLite for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = config('EMAIL_HOST', default='')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
