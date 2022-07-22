#Observaciones:
#Esta configuracion requiere de algunas modificaciones:
    #Instalar Pillow
    #Instalar social-auth-app-django

#Nota sobre los cambios que tiene settings.py respecto al archivo original:
    #Se ha añadido un static_root que no trae por defecto django
    #Se ha añadido import os
    #Se ha añadido el Allowed_host
    #Se ha añadido la app account.apps.AccountConfig
    #Se ha añadido la app social-django
    #El config que trae por defecto para BBDD sqlite es algo diferente, está sustituido
    #Uno de estos dos elementos no estaba y se ha añadido: USE_I18N = True o USE_L10N = True
    #Static_url se ha modificado y añadido contrabarra antes, cosa el setting por defecto no trae.
    #Las 3 variables login se han añadido
    #El sistema de email tanto de terminal(que si se utiliza gmail se deshabilita) como el de gmail se han añadido
    #Los social se ha añadido (pero no están en uso, está por completarse las credenciales. Hay que crear una cuenta developer en cada red social para poder utilizarlos)
    #Para habilitar gmail como servidor smtp https://myaccount.google.com/security y pulsar sobre "Acceso de aplicaciones menos seguras".

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6l2&5-7uq0w_#y7@$+lf@#hk9rjp4q517r-myk&*1jfcjlgz5)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookmarks.urls'

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

WSGI_APPLICATION = 'bookmarks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

#STATIC_URL = 'static/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'


#SERVIDOR DE CORREO (Terminal o por Gmail):

#1.-Para utilizar terminal como servidor de correo:
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend')

#2.-Esto siguiente no se para qué se utilizó:
#EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
#EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')

#3.-Para utilizar la configuración de gmail como servidor de correo (está el email y el password por completar):
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ''  #Poner email de la cuente que hace de servidor de correo.
EMAIL_HOST_PASSWORD = ''  #Poner password de la cuenta que hace de servidor de correo.




AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2',
]

# social auth settings
SOCIAL_AUTH_FACEBOOK_KEY = '' # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '' # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_TWITTER_KEY = '' # Twitter Consumer Key
SOCIAL_AUTH_TWITTER_SECRET = '' # Twitter Consumer Secret

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '' # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '' # Google Consumer Secret
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





