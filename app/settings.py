import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '***REMOVED***'

# Whether the project should be configured in development mode
DEVELOPMENT = False

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DEVELOPMENT

ALLOWED_HOSTS = ['dulno.com', '0.0.0.0']
SECURE_CROSS_ORIGIN_OPENER_POLICY = None

COOKIE_DOMAIN = '.dulno.com'

if DEVELOPMENT:
  COOKIE_DOMAIN = '0.0.0.0'

BACKEND_ENDPOINT = 'http://10.96.0.4'

if DEVELOPMENT:
  BACKEND_ENDPOINT = 'https://api.dulno.com'

# Application definition

INSTALLED_APPS = [
  'base.apps.BaseConfig',
  'whitelist.apps.WhitelistConfig',
  'maintenance.apps.MaintenanceConfig',
  'errors.apps.ErrorsConfig',
  'home.apps.HomeConfig',
  'verification.apps.VerificationConfig',
  'product.apps.ProductConfig',
  'settings.apps.SettingsConfig',
  'ticket.apps.TicketConfig',
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'corsheaders',
]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.locale.LocaleMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'corsheaders.middleware.CorsMiddleware',
  'whitelist.middleware.WhitelistMiddleware',
  'maintenance.middleware.MaintenanceMiddleware',
]

CSRF_TRUSTED_ORIGINS = ["https://dulno.com"]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR + "/templates/"],
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

WSGI_APPLICATION = 'app.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
  BASE_DIR + '/static/',
]

LOCALE_PATHS = (
   BASE_DIR + '/locale/',
)

LANGUAGES = (
  ('en', 'English'),
  ('de', 'Deutsch'),
)

WHITELIST = False

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'handlers': {
    'console': {
      'level': 'DEBUG',
      'class': 'logging.StreamHandler',
    },
    'custom_handler': {
      'level': 'ERROR',
      'class': 'errors.exception.ExceptionHandler',
    },
  },
  'loggers': {
    'django': {
      'handlers': ['console', 'custom_handler'],
      'level': 'DEBUG',
      'propagate': True,
    },
  },
}