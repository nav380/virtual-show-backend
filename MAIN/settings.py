import os
import sys
from django.contrib.messages import constants as messages
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "..", "..", "apps"))

SECRET_KEY = 'django-insecure-&a@s(za*td#ph@ja=vz&k4b=127su)x+#&h%l@i(jnb_w-br_%'

DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Virtual_Showroom_db',
    'Master',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # CORS middleware must come before CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'MAIN.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'MAIN.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'mssql',
#         'NAME': 'is_app_db_new',
#         'USER': 'sa',
#         'PASSWORD': 'Ssc@Admin#123',
#         'HOST': 'SSCREATION\\ISSQLSERVER',
#         'OPTIONS': {'driver': 'ODBC Driver 17 for SQL Server', },
#     },
#     'intellisync_db': {
#         'ENGINE': 'mssql',
#         'NAME': 'is_intellisync_db',
#         'USER': 'sa',
#         'PASSWORD': 'Ssc@Admin#123',
#         'HOST': 'SSCREATION\\ISSQLSERVER',
#         'OPTIONS': {'driver': 'ODBC Driver 17 for SQL Server', },
#     },
#     'erp_db': {
#         'ENGINE': 'mssql',
#         'NAME': 'VisualGEMS',
#         'USER': 'sa',
#         'PASSWORD': 'Ssc@Admin#123',
#         'HOST': 'SSCREATION\\ISSQLSERVER',
#         'OPTIONS': {'driver': 'ODBC Driver 17 for SQL Server', },
#     },
#     'App_db': {
#         'ENGINE': 'mssql',
#         'NAME': 'is_app_db_new',
#         'USER': 'sa',
#         'PASSWORD': 'Ssc@Admin#123',
#         'HOST': 'SSCREATION\\ISSQLSERVER',
#         'OPTIONS': {'driver': 'ODBC Driver 17 for SQL Server', },
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'en-us'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ************ Custom Settings ************

# Indian Timezone
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Reconfigure Static and Media Files Access
ASSETS_DIR = os.path.join(BASE_DIR, '..', '..', 'assets')
STATICFILES_DIRS = [ASSETS_DIR + '/static']
STATIC_URL = 'static/'
STATIC_ROOT = ASSETS_DIR + '/staticfiles'
MEDIA_URL = 'media/'
MEDIA_ROOT = ASSETS_DIR + '/media'

# Session
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 36000  # Session timeout 60*60*10 = 10 Hours

# Redirect to this URL if user is not logged in
LOGIN_URL = '/login/'



# Customize alert message type
MESSAGE_TAGS = {
    messages.ERROR: 'error',
    messages.SUCCESS: 'success',
    messages.INFO: 'info',
    messages.WARNING: 'warning'
}

# Database routers

PROJECT_CODE = 'is_tna'

# ************ CORS Settings ************
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:12002",
    "http://localhost:5173",
]

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:12002",
    "http://localhost:5173",
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
