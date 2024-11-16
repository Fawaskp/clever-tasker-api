from pathlib import Path
from decouple import config,Csv
from datetime import timedelta
import os
    
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('DJANGO_SECRET_KEY')
DEBUG = config('DJANGO_DEBUG',default=False,cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS',cast=Csv())

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

EXTERNAL_APPS = [
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'django_filters',
    "corsheaders",
]

USER_APPS=[
    'auth_handler',
    'tasks',
]

INSTALLED_APPS = DJANGO_APPS+USER_APPS+EXTERNAL_APPS

# DRF settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
     'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

# Simple JWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=5),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': config('DJANGO_SECRET_KEY'),
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
}

# CORS
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS',cast=Csv())
CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'accept',
    'origin',
    'x-requested-with',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
     "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Clevertasker.urls'

# html templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'Clevertasker.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DEFAULT_DB_NAME'),
        'USER': config('DEFAULT_DB_USER'),
        'PASSWORD': config('DEFAULT_DB_PASSWORD'),
        'HOST': config('DEFAULT_DB_HOST'),
        'PORT': config('DEFAULT_DB_PORT'),   
    }
}

# cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'otp_cache',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE =  'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Custom user model
AUTH_USER_MODEL = 'auth_handler.MyUser'

# SMTP
EMAIL_BACKEND=config('EMAIL_BACKEND')
EMAIL_HOST=config('EMAIL_HOST')
EMAIL_PORT=config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER= config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD= config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS=True

APPEND_SLASH = False