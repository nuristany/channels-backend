from decouple import config
from .common import *

# Secret Key
SECRET_KEY = config('SECRET_KEY')

# Debug mode
DEBUG = config('DEBUG', default=False, cast=bool)

# Allowed hosts
ALLOWED_HOSTS = [
    "your-production-domain.com",
    "channels-backend-production.up.railway.app",
]

# CSRF trusted origins
CSRF_TRUSTED_ORIGINS = [
    "https://your-production-domain.com",
    "https://channels-backend-production.up.railway.app",
]

# CORS
CORS_ALLOWED_ORIGINS = [
    "https://channels-backend-production.up.railway.app",
    'channels-backend-production.up.railway.app',
    "https://django-chat.netlify.app",
]

# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SAMESITE = 'Lax'

# Secure SSL redirect
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Static files (optional: aggressive caching headers for production)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
