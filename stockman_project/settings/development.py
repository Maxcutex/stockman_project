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
		'NAME': os.environ.get('DATABASE_NAME', ''),
		'USER': os.environ.get('DATABASE_USER', ''),
		'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
		'HOST': os.environ.get('DATABASE_HOST', ''),
		'PORT': os.environ.get('DATABASE_PORT', ''),
		'TEST': {
			'NAME': os.environ.get('DATABASE_NAME_TEST', ''),
		},
	}
}
