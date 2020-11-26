"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
import django_heroku
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'ngq_-l*jo65fydj!g_0%8ko^5az_0*c_!a2sqi4-_)o+k9xf&*'
import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'ngq_-l*jo65fydj!g_0%8ko^5az_0*c_!a2sqi4-_)o+k9xf&*')
# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

      #'phone_field',
     'storages',
    'catalog',
    'crispy_forms',

    'cloudinary_storage',
    'cloudinary',
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

ROOT_URLCONF = 'ecommerce.urls'

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

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'moonstore',
        'USER': 'postgres',
        'PASSWORD': 'bb99GG00',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/images/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')


AWS_ACCESS_KEY_ID = 'AKIAIBBGI3HYFGVI7GJQ'
AWS_STORAGE_BUCKET_NAME = 'benstar-bucket'
AWS_SECRET_ACCESS_KEY = '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'


AWS_UPLOAD_USERNAME = "BEN_user_jomusi"
AWS_UPLOAD_REGION = 'us-west-2'
AWS_UPLOAD_GROUP = "BEN_AwesomeGroup"


AWS_DEFAULT_ACL = None
AWS_S3_FILE_OVERWRITE = False

STATIC_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'ecommerce.storage_backends.MediaStorage'


STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

"""AWS_UPLOAD_BUCKET = "benstar-bucket"

AWS_UPLOAD_USERNAME = "BEN_user_jomusi"

AWS_UPLOAD_GROUP = "BEN_AwesomeGroup"


AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

AWS_UPLOAD_REGION = 'us-west-2'

AWS_UPLOAD_ACCESS_KEY_ID = "AKIAIBBGI3HYFGVI7GJQ"

AWS_UPLOAD_SECRET_KEY = "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 "

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_UPLOAD_BUCKET
#AWS_S3_REGION_NAME = 'us-east-2'
#AWS_S3_SIGNATURE_VERSION = 's3v4'  """

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'home'

# Activate Django-Heroku.
django_heroku.settings(locals())

