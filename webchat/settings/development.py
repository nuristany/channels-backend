from .common import *
from decouple import config

# Secret Key
SECRET_KEY = config('SECRET_KEY')

# Always True in development
DEBUG = config('DEBUG', default=True, cast=bool)

# Development-only settings
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.1.106']

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://192.168.1.106:5173',
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:5173',
    'http://192.168.1.106:5173',
]

# Local SQLite database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

EMAIL_BACKEND=config('EMAIL_BACKEND')
EMAIL_HOST=config('EMAIL_HOST')
EMAIL_PORT=config('EMAIL_PORT')
EMAIL_HOST_USER=config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS=config('EMAIL_USE_TLS', default=True, cast=bool)
