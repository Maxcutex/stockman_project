"""
Django settings for stockman_project project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from datetime import timedelta

from dj_database_url import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '21)^n6=5y$ams&oyqlumbhbaqthx9y+)p=9_&f30tgb-$uibhu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'rest_framework',
	'rest_framework.authtoken',
	'stock_setup_info',
	'stock_profile_mgt', 'stock_maintain', 'django_filters',
	'import_export', 'corsheaders', 'ckeditor', 'ckeditor_uploader',
	'rest_auth',
	'rest_auth.registration',
	'django.contrib.sites',
	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	'allauth.socialaccount.providers.agave',
	'allauth.socialaccount.providers.amazon',
	'allauth.socialaccount.providers.angellist',
	'allauth.socialaccount.providers.asana',
	'allauth.socialaccount.providers.auth0',
	'allauth.socialaccount.providers.authentiq',
	'allauth.socialaccount.providers.baidu',
	'allauth.socialaccount.providers.basecamp',
	'allauth.socialaccount.providers.bitbucket',
	'allauth.socialaccount.providers.bitbucket_oauth2',
	'allauth.socialaccount.providers.bitly',
	'allauth.socialaccount.providers.cern',
	'allauth.socialaccount.providers.coinbase',
	'allauth.socialaccount.providers.dataporten',
	'allauth.socialaccount.providers.daum',
	'allauth.socialaccount.providers.digitalocean',
	'allauth.socialaccount.providers.discord',
	'allauth.socialaccount.providers.disqus',
	'allauth.socialaccount.providers.douban',
	'allauth.socialaccount.providers.draugiem',
	'allauth.socialaccount.providers.dropbox',
	'allauth.socialaccount.providers.dwolla',
	'allauth.socialaccount.providers.edmodo',
	'allauth.socialaccount.providers.eveonline',
	'allauth.socialaccount.providers.evernote',
	'allauth.socialaccount.providers.facebook',
	'allauth.socialaccount.providers.feedly',
	'allauth.socialaccount.providers.fivehundredpx',
	'allauth.socialaccount.providers.flickr',
	'allauth.socialaccount.providers.foursquare',
	'allauth.socialaccount.providers.fxa',
	'allauth.socialaccount.providers.github',
	'allauth.socialaccount.providers.gitlab',
	'allauth.socialaccount.providers.google',
	'allauth.socialaccount.providers.hubic',
	'allauth.socialaccount.providers.instagram',
	'allauth.socialaccount.providers.kakao',
	'allauth.socialaccount.providers.line',
	'allauth.socialaccount.providers.linkedin',
	'allauth.socialaccount.providers.linkedin_oauth2',
	'allauth.socialaccount.providers.mailru',
	'allauth.socialaccount.providers.mailchimp',
	'allauth.socialaccount.providers.meetup',
	'allauth.socialaccount.providers.naver',
	'allauth.socialaccount.providers.odnoklassniki',
	'allauth.socialaccount.providers.openid',
	'allauth.socialaccount.providers.orcid',
	'allauth.socialaccount.providers.paypal',
	'allauth.socialaccount.providers.persona',
	'allauth.socialaccount.providers.pinterest',
	'allauth.socialaccount.providers.reddit',
	'allauth.socialaccount.providers.robinhood',
	'allauth.socialaccount.providers.shopify',
	'allauth.socialaccount.providers.slack',
	'allauth.socialaccount.providers.soundcloud',
	'allauth.socialaccount.providers.spotify',
	'allauth.socialaccount.providers.stackexchange',
	'allauth.socialaccount.providers.stripe',
	'allauth.socialaccount.providers.trello',
	'allauth.socialaccount.providers.tumblr',
	'allauth.socialaccount.providers.twentythreeandme',
	'allauth.socialaccount.providers.twitch',
	'allauth.socialaccount.providers.twitter',
	'allauth.socialaccount.providers.untappd',
	'allauth.socialaccount.providers.vimeo',
	'allauth.socialaccount.providers.vimeo_oauth2',
	'allauth.socialaccount.providers.vk',
	'allauth.socialaccount.providers.weibo',
	'allauth.socialaccount.providers.weixin',
	'allauth.socialaccount.providers.windowslive',
	'allauth.socialaccount.providers.xing',

]
SITE_ID = 1
MIDDLEWARE = [
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'stockman_project.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'stockman_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIR = (
	os.path.join(BASE_DIR, "static"),
	'/static/',
)

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

CKEDITOR_UPLOAD_PATH = "uploads/"

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
	'localhost:8000',
	'localhost:3000',
	'127.0.0.1:9000'
)
CORS_ORIGIN_REGEX_WHITELIST = (
	'localhost:8000',
	'localhost:3000',
	'127.0.0.1:9000'
)
CORS_ALLOW_METHODS = (
	'DELETE',
	'GET',
	'OPTIONS',
	'PATCH',
	'POST',
	'PUT',
)
CORS_ALLOW_HEADERS = (
	'accept',
	'accept-encoding',
	'authorization',
	'content-type',
	'dnt',
	'origin',
	'user-agent',
	'x-csrftoken',
	'x-requested-with',
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'stock_profile_mgt.UserProfile'

REST_FRAMEWORK = {
	'DATE_INPUT_FORMATS': ['iso-8601', '%Y-%m-%d'],
	'DEFAULT_PERMISSION_CLASSES': (
		'stockman_project.permissions.IsGetOrIsAuthenticated',
	),
	# 'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),
	'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_jwt.authentication.JSONWebTokenAuthentication',),
	# 'DEFAULT_PERMISSION_CLASSES': [], set to null to enable view based permissions per views
	'DEFAULT_FILTER_BACKENDS': (
		'django_filters.rest_framework.DjangoFilterBackend',),
	'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
	'PAGE_SIZE': 10
}
USERNAME = None
IMPORT_EXPORT_USE_TRANSACTIONS = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = True

# rest-auth
# ACCOUNT_ADAPTER = 'api.adapter.DefaultAccountAdapterCustom'
URL_FRONT = 'http://localhost:8000/'
LOGIN_URL='/api/v1/login/'
# LOGIN_URL = 'http://stockman-api.herokuapp.com/api/v1/login/'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = LOGIN_URL
ACCOUNT_PASSWORD_RESET_CONFIRM = LOGIN_URL + 'password-reset/confirm/'

REST_USE_JWT = True
REST_AUTH_REGISTER_SERIALIZERS = {
	'REGISTER_SERIALIZER': 'stock_profile_mgt.serializers.RegisterSerializerCustom',

}
REST_AUTH_SERIALIZERS = {
	'USER_DETAILS_SERIALIZER': 'stock_profile_mgt.serializers.UserProfileSerializer',
	'PASSWORD_RESET_SERIALIZER': 'stock_profile_mgt.serializers.PasswordSerializer',
}

JWT_AUTH = {
	'JWT_ALLOW_REFRESH': True,
	'JWT_EXPIRATION_DELTA': timedelta(days=7),
	'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
	'JWT_AUTH_HEADER_PREFIX': 'Bearer',
	# 'JWT_SECRET_KEY': config(SECRET_KEY, default=''),
}

EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'tmp/email')
