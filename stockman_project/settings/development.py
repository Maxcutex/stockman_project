from .base import *

DEBUG = True

INSTALLED_APPS += ()

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=stockman_project, stock_setup_info, stock_profile_mgt',
]
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# configure your database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', ''),
        'USER': os.environ.get('DATABASE_USER', ''),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
        'TEST': {
            'NAME': os.environ.get('DATABASE_NAME_TEST', ''),
        },
    }
}
# HOST_NAME = os.environ.get('HOST_NAME')
# ALLOWED_HOSTS += [HOST_NAME]
LOGIN_URL = 'http://127.0.0.1/login/'
SITE_ID = 2
