from decouple import config
from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# Allowed Hosts
ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])


# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    "https://channels-backend-production.up.railway.app",
]

# CORS
CORS_ALLOWED_ORIGINS = [
    "https://channels-backend-production.up.railway.app",
    "https://django-chat.netlify.app",
]

# Database (already handled in common.py if using dj-database-url or similar)

# Email backend
EMAIL_BACKEND = config("EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend")
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT", cast=int)
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool)
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Celery broker (used in celery.py if imported)
CELERY_BROKER_URL = config("CELERY_BROKER_URL")

# Security settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SAMESITE = 'Lax'

# HTTPS support behind reverse proxy (like Railway)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Static file storage
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# prod.py
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Make sure this matches the volume path
