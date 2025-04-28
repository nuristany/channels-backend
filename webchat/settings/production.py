from decouple import config
from .common import *

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ["your-production-domain.com", "channels-backend-production.up.railway.app"]

CSRF_TRUSTED_ORIGINS = [
    "https://your-production-domain.com",
    "https://channels-backend-production.up.railway.app",
]

CORS_ALLOWED_ORIGINS = [
    "https://your-production-domain.com",
    "http://localhost:5173",
    "https://django-chat.netlify.app",
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SAMESITE = 'Lax'

# DATABASES is already loaded from common.py using DATABASE_URL
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")