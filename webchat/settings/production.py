import os
from .common import *
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False


CSRF_TRUSTED_ORIGINS = [
    "https://channels-backend-production.up.railway.app",
    "https://your-frontend-domain.com"
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://your-frontend-domain.com"
]
