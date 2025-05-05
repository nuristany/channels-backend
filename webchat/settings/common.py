from pathlib import Path
from datetime import timedelta
import os
from decouple import config
import dj_database_url

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',

    'corsheaders',
    'djoser',
    'rest_framework',

    'accounts',
    'chat',
]

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://192.168.1.106:5173",
    "https://channels-backend-production.up.railway.app",
    "https://django-chat.netlify.app",
]
CORS_ALLOW_CREDENTIALS = True

# CSRF trusted origins
CSRF_TRUSTED_ORIGINS = [
    "https://channels-backend-production.up.railway.app",
    "http://192.168.1.106:5173",
    "http://192.168.1.106",
    "http://localhost:5173",
]

# Allowed hosts
ALLOWED_HOSTS = [
    'channels-backend-production.up.railway.app',
    'localhost',
    '127.0.0.1',
    '192.168.1.106',
]

# Templates
ROOT_URLCONF = 'webchat.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'webchat.wsgi.application'
ASGI_APPLICATION = 'webchat.asgi.application'

# Database
# DATABASES = {
#     'default': dj_database_url.config(default=config('DATABASE_URL'))
# }

default_db = (
    'sqlite:///db.sqlite3' if os.environ.get('RUNNING_IN_DOCKER_BUILD')
    else config('DATABASE_URL')
)

DATABASES = {
    'default': dj_database_url.config(default=default_db)
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static and Media files
# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] 

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model
AUTH_USER_MODEL = 'accounts.UserAccount'

# Django Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # 'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],  # Uncomment if needed
}



# JWT
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
}

# settings.py
PASSWORD_RESET_TIMEOUT = 60 



# Channels
# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels.layers.InMemoryChannelLayer',
#     },
# }

DJOSER = {
    'SERIALIZERS': {
        'user_create': 'accounts.serializers.CustomeUserCreateSerializer',  # use your full path
    }
}


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
        },
    },
}

CELERY_BROKER_URL = 'redis://redis:6379/1'


# Security settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SAMESITE = 'Lax'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)



FRONTEND_URL = "http://localhost:3000"  # or your real frontend URL

from celery.schedules import crontab
CELERY_BEAT_SCHEDULE = {
    'delete_expired_inactive_users_task': {
        'task': 'accounts.tasks.delete_expired_inactive_users',  # Task you just created
         'schedule': crontab(minute='*/5'), 
    },
}
