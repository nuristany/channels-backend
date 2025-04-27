from .common import *

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

# No need to redefine DATABASES — already loaded from common.py
