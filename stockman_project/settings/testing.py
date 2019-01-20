# -*- coding: utf-8 -*-
from .base import *

DEBUG = True

INSTALLED_APPS += ('django_nose',)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
	'--with-coverage',
	'--cover-package=stockman_project, stock_setup_info, stock_profile_mgt',
]

ALLOWED_HOSTS = ['*']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
