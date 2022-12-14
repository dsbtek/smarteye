"""
Django settings for atg_web project.

Generated by 'django-admin startproject' using Django 2.0.9.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
from corsheaders.defaults import default_headers
import os
from datetime import timedelta
from decouple import config
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)


#Config for APM with sentry
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.redis import RedisIntegration

CORS_ALLOW_HEADERS = list(default_headers) + [
    "Access-Control-Allow-Origin",
]
CORS_ORIGIN_ALLOW_ALL = True

sentry_sdk.init(
    dsn="https://7433389d04c3486b8d0d83b6474f22f7@sentry.io/1770167",
    integrations=[DjangoIntegration(), CeleryIntegration(), RedisIntegration()],
    environment= config('ENVIRONMENT')
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Third-party Apps
    'rest_framework',
    'corsheaders',
    'drf_spectacular',

    #Local Apps
    'backend.apps.BackendConfig',
    'test_without_migrations',
    'django_crontab',
    'auditlog'
]

MIDDLEWARE = [
    
    #'request_logging.middleware.LoggingMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'backend.custommiddleware.MyAuditCustomMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
    # 'backend.request_log_middleware.RequestLogMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
	    'PASSWORD': config('DB_PASSWORD'),
	    'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
        
    },
    'station_manager': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('SM_DB_NAME'),
        'USER': config('SM_DB_USER'),
	    'PASSWORD': config('SM_DB_PASSWORD'),
	    'HOST': config('SM_DB_HOST'),
        'PORT': config('SM_DB_PORT'),
    }
}

ROOT_URLCONF = 'atg_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'atg_web.wsgi.application'

#USER MODEL
AUTH_USER_MODEL = 'backend.User'


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'backend.permissions.IsActiveAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'EXCEPTION_HANDLER': 'backend.custom_exception_handler.my_exception_handler',
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S",
    #'DATETIME_FORMAT': "%y-%m-%d %I:%M:%S %p",
    #'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    #'PAGE_SIZE': 5

}

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [    
    os.path.join(BASE_DIR, "static"),
]


MEDIA_URL =  '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

SPECTACULAR_SETTINGS = {
    'SCHEMA_PATH_PREFIX': r'/api/v[0-9]',
    'TITLE': 'Smarteye API',
    'DESCRIPTION': 'An interactive documentation of the entire smart-eye-api (each endpoint grouped into its module category).',
    'VERSION': '0.0.1',
    'SERVE_INCLUDE_SCHEMA': False,
    'SERVE_PERMISSIONS': [],
}


CRONJOBS = [
    #('0 23 * * *', 'backend.reports.cron.anomaly.main', '>> /var/log/anomaly.log'),
    #('45 23 * * *', 'backend.reports.cron.missed_logs_anomaly_detector.main', '>> missed_log.log'),
    
 
]

CRONTAB_COMMAND_SUFFIX = '2>&1'
REDIS_HOST = 'prodsmarti.lbzjml.ng.0001.use2.cache.amazonaws.com'
REDIS_PORT = '6379'
RABBIQ_MQ_URL = 'http://smarteye_prod_heartbeat_user:vt6Su59PBe8^@cupid.smartflowtech.com:15672'



