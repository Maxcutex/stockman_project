"""
Django settings for stockman_project project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import pdb
import platform

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys
from datetime import timedelta
from pathlib import Path

# from decouple import config
# import dj_database_url
# import urllib.parse as urlparse
from urllib.parse import urlparse


CHECK_DIR = Path(__file__).parent.parent.parent
# BASE_DIR = Path(__file__).parent.parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# print(os.environ, "<=== OS")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "21)^n6=5y$ams&oyqlumbhbaqthx9y+)p=9_&f30tgb-$uibhu"
# SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    "0.0.0.0",
    "localhost",
    "localhost:3000",
    "127.0.0.1",
    "stockman-api.herokuapp.com",
    "api",
    "https://stockmanreact.ennyboy.now.sh/",
    "https://elasticbeanstalk-us-east-2-606297809594.s3.amazonaws.com/",
    "https://stockman-frontend.herokuapp.com/",
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    # 'rest_framework_swagger',
    "drf_yasg",
    "rest_framework.authtoken",
    "stock_setup_info",
    "stock_profile_mgt",
    "stock_maintain",
    "django_filters",
    "search_indexes",
    "import_export",
    "corsheaders",
    "ckeditor",
    "ckeditor_uploader",
    "rest_auth",
    "rest_auth.registration",
    "django.contrib.sites",
    "admin_ordering",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.amazon",
    "allauth.socialaccount.providers.auth0",
    "allauth.socialaccount.providers.baidu",
    "allauth.socialaccount.providers.basecamp",
    "allauth.socialaccount.providers.bitbucket",
    "allauth.socialaccount.providers.digitalocean",
    "allauth.socialaccount.providers.dropbox",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.flickr",
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.gitlab",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.instagram",
    "allauth.socialaccount.providers.linkedin",
    "allauth.socialaccount.providers.linkedin_oauth2",
    "allauth.socialaccount.providers.mailru",
    "allauth.socialaccount.providers.mailchimp",
    "allauth.socialaccount.providers.openid",
    "allauth.socialaccount.providers.paypal",
    "allauth.socialaccount.providers.pinterest",
    "allauth.socialaccount.providers.reddit",
    "allauth.socialaccount.providers.shopify",
    "allauth.socialaccount.providers.slack",
    "allauth.socialaccount.providers.spotify",
    "allauth.socialaccount.providers.stackexchange",
    "allauth.socialaccount.providers.tumblr",
    "allauth.socialaccount.providers.twitter",
    # Django Elasticsearch integration
    "django_elasticsearch_dsl",
    # Django REST framework Elasticsearch integration (this package)
    "django_elasticsearch_dsl_drf",
    # for uploading
    "storages",
    # 'rangefilter',
    "celery",
]
SITE_ID = 1
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Name of the Elasticsearch index
ELASTICSEARCH_INDEX_NAMES = {
    "search_indexes.documents.news": "news",
    "search_indexes.documents.stock": "stock",
}
ES_URL = urlparse(os.environ.get("BONSAI_URL") or "http://127.0.0.1:9200/")

# port = ES_URL.port or 80
# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
#         'URL': ES_URL.scheme + '://' + ES_URL.hostname + ':'+ str(port),
#         'INDEX_NAME': 'haystack',
#     },
# }
#
# if ES_URL.username:
#     HAYSTACK_CONNECTIONS['default']['KWARGS'] = {"http_auth": ES_URL.username + ':' + ES_URL.password}

ROOT_URLCONF = "stockman_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "stockman_project.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Lagos"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

USE_S3 = os.getenv("USE_S3") == "TRUE"

if USE_S3:
    # aws settings
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_DEFAULT_ACL = "public-read"
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
    TEXT_CKEDITOR_BASE_PATH = (
        f"https://{AWS_S3_CUSTOM_DOMAIN}/djangocms_text_ckeditor/ckeditor/"
    )
    # s3 static settings
    AWS_LOCATION = "static"
    AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"
    STATICFILES_STORAGE = "stockman_project.storage_backends.StaticStorage"
    CKEDITOR_BASEPATH = f"{STATIC_URL}ckeditor/ckeditor/"

    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = "media"
    PUBLIC_CSV_LOCATION = "csv_uploads"
    # MEDIA_ROOT = '..' + os.path.join(CHECK_DIR, 'media')
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_CSV_LOCATION}/"
    DEFAULT_FILE_STORAGE = "stockman_project.storage_backends.PublicMediaStorage"
else:
    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    MEDIA_ROOT = ".." + os.path.join(CHECK_DIR, "media")
    MEDIA_URL = "/media/"
    CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
STATICFILES_DIR = (
    os.path.join(BASE_DIR, "static"),
    # '/static/',
)


CKEDITOR_UPLOAD_PATH = "uploads/"

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    "localhost:8000",
    "localhost:3000",
    "127.0.0.1:9000",
    "https://elasticbeanstalk-us-east-2-606297809594.s3.amazonaws.com/",
    "https://stockmanreact.ennyboy.now.sh/",
)
CORS_ORIGIN_REGEX_WHITELIST = (
    "localhost:8000",
    "localhost:3000",
    "127.0.0.1:9000",
    "https://elasticbeanstalk-us-east-2-606297809594.s3.amazonaws.com/",
    "https://stockmanreact.ennyboy.now.sh/",
)
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)
CORS_ALLOW_HEADERS = (
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
)


AUTH_USER_MODEL = "stock_profile_mgt.UserProfile"

REST_FRAMEWORK = {
    "DATE_INPUT_FORMATS": ["iso-8601", "%Y-%m-%d"],
    # 'DEFAULT_PERMISSION_CLASSES': (
    # 	'stockman_project.permissions.IsGetOrIsAuthenticated',
    # ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
    ),
    # 'DEFAULT_PERMISSION_CLASSES': [], set to null to enable view based permissions per views
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'DEFAULT_PAGINATION_CLASS': 'stockman_project.DefaultResultsSetPagination',
    "PAGE_SIZE": 10,
}
USERNAME = None
IMPORT_EXPORT_USE_TRANSACTIONS = True

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = config('EMAIL_PORT')
# EMAIL_USE_TLS = True

# EMAIL_HOST = 'server96.web-hosting.com'
# EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = 'customercare@marketsmithonline.com'
# EMAIL_HOST_PASSWORD ='Olubanke@1'
# EMAIL_PORT = 25
# EMAIL_USE_TLS = False

EMAIL_HOST = "127.0.0.1"
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 1025
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False

# rest-auth
# ACCOUNT_ADAPTER = 'api.adapter.DefaultAccountAdapterCustom'
URL_FRONT = "http://localhost:3000/"
LOGIN_URL = "http:///fronten.com/"
# LOGIN_URL = 'http://stockman-api.herokuapp.com/api/v1/login/'
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = LOGIN_URL
ACCOUNT_PASSWORD_RESET_CONFIRM = LOGIN_URL + "password-reset/confirm/"

REST_USE_JWT = True
REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "stock_profile_mgt.serializers.RegisterSerializerCustom",
}
REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "stock_profile_mgt.serializers.UserProfileSerializer",
    "PASSWORD_RESET_SERIALIZER": "stock_profile_mgt.serializers.PasswordSerializer",
}

JWT_AUTH = {
    "JWT_ALLOW_REFRESH": True,
    "JWT_EXPIRATION_DELTA": timedelta(days=7),
    "JWT_REFRESH_EXPIRATION_DELTA": timedelta(days=7),
    "JWT_AUTH_HEADER_PREFIX": "Bearer",
    # 'JWT_SECRET_KEY': config(SECRET_KEY, default=''),
}

EMAIL_FILE_PATH = os.path.join(BASE_DIR, "tmp/email")
ELASTIC_HOST_NAME = os.environ.get("ELASTIC_HOST_NAME", "localhost")
ELASTIC_HOST_PORT = os.environ.get("ELASTIC_HOST_PORT", "9200")

ELASTICSEARCH_DSL = {
    "default": {"hosts": ELASTIC_HOST_NAME + ":" + ELASTIC_HOST_PORT},
}

CACHE_TTL = 60 * 1  # 1 minute


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get(
            "REDIS_URL", "localhost"
        ),  # "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

if "test" in sys.argv:
    CACHES = {
        "default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"},
    }

# Celery Settings

# Celery settings

CELERY_BROKER_URL = os.environ.get("REDIS_URL", "localhost")
#
# #: Only add pickle to this list if your broker is secured
# #: from unwanted access (see userguide/security.html)
# CELERY_ACCEPT_CONTENT = ['json']
# # CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'
# # CELERY_RESULT_BACKEND=os.environ['REDIS_URL']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'Africa/Lagos'

BROKER_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")
CELERY_RESULT_BACKEND = os.environ.get("REDIS_URL", "redis://localhost:6379")
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "Africa/Lagos"
