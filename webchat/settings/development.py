from dotenv import load_dotenv
load_dotenv()
import os

from .common import *
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
