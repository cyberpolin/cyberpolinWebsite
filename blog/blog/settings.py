"""
Django settings for blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jbd+wrye&s1acl!=^rjf!pkgyivm7s&guy6@p4fct^^8)xj=pp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['.cyberpolin.com']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'froala_editor',
    'articulos',
#    'rest_framework',
#    'djangular'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'blog.urls'

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'file': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cyberpolin',
        'USER': 'postgres',
        'PASSWORD': 'rt459Pk1',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }

}

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'blog/fixtures/'),
)


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/home/django/cyberpolinWebsite/blog/static',
]
MEDIA_URL = '/media/'
MEDIA_ROOT = '/media/'

MEDIAFILES_DIRS = [
    os.path.join(BASE_DIR, "media"),
    '/home/django/cyberpolinWebsite/blog/static',
]


TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), '../templates'),
)
#Claves de logeo
LOGIN_REDIRECT_URL = "/admin/articulos"
# Redirect when login is not correct.
LOGIN_URL = '/admin/login/'

#REST_API

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# MAIL
# EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'hire@cyberpolin.com'
EMAIL_HOST_PASSWORD = 'rt459pk1'
EMAIL_PORT = 587
# DEFAULT_FROM_EMAIL = 'cyberpolin@gmail.com'
