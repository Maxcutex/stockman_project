from .base import *

DEBUG = True

INSTALLED_APPS += ()

# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
	'--with-coverage',
]

# configure your database
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': os.environ.get('DATABASE_NAME', 'marketsmith_db'),
        'USER': os.environ.get('DATABASE_USER', 'marketsmith_user'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'olubanke@1'),
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
		'TEST': {
			'NAME': os.environ.get('DATABASE_NAME_TEST', 'marketsmith_db_test'),
		},
	}
}
