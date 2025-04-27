
from pathlib import Path
from datetime import timedelta
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'djoser',
    'rest_framework',
    'accounts',
    'chat',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware", 
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Allow requests from your React app
    "http://192.168.1.106:5173",  # Allow requests from other devices on the same network
   
]



CORS_ALLOW_CREDENTIALS = True  # Allow cookies and authentication headers


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


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}


CSRF_TRUSTED_ORIGINS = [
    "https://channels-backend-production.up.railway.app", 
    "http://192.168.1.106:5173",
    "http://192.168.1.106",
    "http://localhost:5173",

    ]
ALLOWED_HOSTS = [
    'channels-backend-production.up.railway.app',
    "localhost", "127.0.0.1", "192.168.1.106",
    "http://localhost:5173",
    ]


AUTH_USER_MODEL = 'accounts.UserAccount'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ),

    # 'DEFAULT_PERMISSION_CLASSES' : [
    #     'rest_framework.permissions.IsAuthenticated'
    # ]
}

SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('Bearer',),
   'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
   
}


CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SAMESITE = 'Lax'


from decouple import config
# import urllib.parse as urlparse
# url = urlparse.urlparse(config('DATABASE_URL'))

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': url.path[1:],  # database name without the leading '/'
#         'USER': url.username,
#         'PASSWORD': url.password,
#         'HOST': url.hostname,
#         'PORT': url.port,
#     }
# }

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}