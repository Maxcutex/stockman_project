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
		'NAME': 'marketsmith_db',
		'USER': 'marketsmith_user',
		'PASSWORD': 'olubanke@1',
		'HOST': 'localhost',
		'PORT': '5432',
		'TEST': {
			'NAME': 'marketsmith_db_test',
		},
	}
}
