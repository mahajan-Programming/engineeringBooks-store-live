"""
Django settings for BuyAndSell project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import gzip
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't6_@lhkba4ne0g3e6y4#xxz8nowhf&*8cr0ij+(!b3$f3p%*h0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['buy-n--sell.herokuapp.com','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages', 
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'import_export',
    'userRegistration',    
    "crispy_forms",
    'storages',
    'django_jinja',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BuyAndSell.urls'

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


TEMPLATES = [
     { 
        'BACKEND':'django.template.backends.jinja2.Jinja2',
        'DIRS': ['%s/jinjatemplates/'% (PROJECT_DIR),],
        'APP_DIRS': True,
        },
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

WSGI_APPLICATION = 'BuyAndSell.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'buyNsellDatabase',
        'USER': 'postgres',
        'PASSWORD':'pano2222',
        'HOST':'localhost'
    }
}
import dj_database_url
from openpyxl import xml
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,  'static-root')
]
MEDIA_ROOT = os.path.join(BASE_DIR,  'media')
MEDIA_URL = '/media/'


CRISPY_TEMPLATE_PACK = 'bootstrap4'


LOGIN_REDIRECT_URL = '/'



AWS_ACCESS_KEY_ID = 'AKIASP2GXDQFKSH7GPFW'

AWS_SECRET_ACCESS_KEY = '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'


AWS_STORAGE_BUCKET_NAME = 'django-buy-n--sell-files'

AWS_S3_FILE_OVERWRITE = False

AWS_DEFAULT_ACL = None
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_IS_GZIPPED =True

COMPRESS_STORAGE = STATICFILES_STORAGE

SITE_ID = 2