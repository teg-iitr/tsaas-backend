"""
Django settings for transport project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

"""
This a temp settings file.
You should create your own local_settings.py file. 
You can use this file as a guide to create your 
own local_settings file.

We have written some instructions on how to do this.
Look for comments starting with --->
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# ---> YOU MUST EDIT THIS SECRET KEY. YOU COULD USE ENVIRONMENT VARIABLES
#      TO STORE THIS SECRET KEY
SECRET_KEY = 'gpmb%%4(+856tru7qgq8-$8!v-*)t&_zt=s%&zx2vphrh##9s-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ---> ENTER THE ADDRESS OF THE HOST/DOMAIN NAME THAT DJANGO SHOULD SERVE
#        (e.g. 'www.example.com') '*' WILL ALLOW ANYONE TO MAKE A GET/POST REQUEST
ALLOWED_HOSTS = ['10.19.0.100','http://tsaas.iitr.ac.in','https://tsaas.iitr.ac.in']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'transdb',
]

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

ROOT_URLCONF = 'transport.urls'

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

WSGI_APPLICATION = 'transport.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


# ---> WE ARE USING POSTGRES AS RECOMMENDED BY DJANGO.
#      
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'name_of_database', # ---> REPLACE THIS WITH THE NAME OF YOUR OWN DATABASE
	'USER': 'dummy_username', # ---> REPLACE THIS WITH THE USERNAME YOU CREATE IN PSQL
	'PASSWORD': 'dummy_password', # ---> REPLACE THIS WITH THE PASSWORD YOU CREATE IN PSQL
	'HOST': 'localhost',
	'PORT': '',
    }
}

# ---> YOU CAN USE SQLITE IF YOU WANT TO. THIS IS NOT RECOMMENDEND.
#        JUST UNCOMMENT THE CODE BELOW

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'sqlite3.db',                      # Or path to database file if using sqlite3.
#         'USER': '',                      # Not used with sqlite3.
#         'PASSWORD': '',                  # Not used with sqlite3.
#         'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static/')


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.AllowAny'
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

CORS_ORIGIN_ALLOW_ALL = True

# ---> SET ABOVE TO FALSE AND ADD A TUPLE CONTAINING WEBSITES THAT SHOULD BE ALLOWED

# CORS_ORIGIN_ALLOW_ALL = False

# CORS_ORIGIN_WHITELIST = (
#     'http//:localhost:8000',
# )