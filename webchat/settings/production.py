import os
from .common import *
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['channels-backend-production.up.railway.app']
CSRF_TRUSTED_ORIGINS = ['https://channels-backend-production.up.railway.app']