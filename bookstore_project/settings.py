"""
Django settings for bookstore_project project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import socket
from dotenv import load_dotenv
load_dotenv()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
ENVIRONMENT=os.getenv('ENVIRONMENT',default='development')
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'orders.apps.OrdersConfig',#local
    'books.apps.BooksConfig',#local
    'pages.apps.PagesConfig',#local
    'users.apps.UsersConfig',#local
    'crispy_forms',#third party
    'allauth',#3rd party
    'allauth.account',#3rd party
    'debug_toolbar',#3rd party
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware', # new 
    'django.middleware.cache.UpdateCacheMiddleware', # new 
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware', # new
    'django.middleware.cache.FetchFromCacheMiddleware', # new

]
CACHE_MIDDLEWARE_ALIAS = 'default' 
CACHE_MIDDLEWARE_SECONDS = 604800 
CACHE_MIDDLEWARE_KEY_PREFIX = ''


ROOT_URLCONF = 'bookstore_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'bookstore_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER':'postgres',
        'PASSWORD':'postgres',
        'HOST':'localhost',
        'PORT':''
    }
}


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

STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static'),]
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
AUTH_USER_MODEL='users.CustomUser'
LOGIN_REDIRECT_URL='home'
ACCOUNT_LOGOUT_REDIRECT='home'
CRISPY_TEMPLATE_PACK='bootstrap4'
SITE_ID=1
AUTHENTICATION_BACKENDS=(
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
ACCOUNT_USERNAME_REQUIRED=False
ACCOUNT_AUTHENTICATION_METHOD='email'
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_UNIQUE_EMAIL=True
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL='admin@djangobookstore.com'
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
STRIPE_TEST_PUBLISHABLE_KEY=os.getenv("STRIPE_TEST_PUBLISHABLE_KEY")
STRIPE_TEST_SECRET_KEY=os.getenv("STRIPE_TEST_SECRET_KEY")
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]
if ENVIRONMENT=='production':
    SECURE_BROWSER_XSS_FILTER=True
    X_FRAME_OPTIONS = 'DENY' # new
    SECURE_SSL_REDIRECT = True # new
    SECURE_HSTS_SECONDS = 3600 # new 
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True # new 
    SECURE_HSTS_PRELOAD = True # new
    SESSION_COOKIE_SECURE = True # new 
    CSRF_COOKIE_SECURE = True # new
    SECURE_CONTENT_TYPE_NOSNIFF = True # new

import dj_database_url 
db_from_env = dj_database_url.config(conn_max_age=500) 
DATABASES['default'].update(db_from_env)



