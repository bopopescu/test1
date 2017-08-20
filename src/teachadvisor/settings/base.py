"""
Django settings for teachadvisor project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# confidential
SECRET_KEY = '_*8l#5sz8b@u-4=k(yfgo35e^@)==bom+tacb(&vo!r7b6_+04'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
















TYPE = "base"

# using gmail
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "Balancedtechsgp@gmail.com"
EMAIL_MAIN = "Balancedtechsgp"
EMAIL_HOST_PASSWORD = "fakeready23"
EMAIL_PORT = 587
EMAIL_USE_TLS = True





# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

#necessary for django allauth
    'django.contrib.sites',
#necessary for django ses
    'django_ses',

#installed apps
    'crispy_forms',
    'django_cleanup',

    'home',
    # 'student',
    # 'teacher',
    # 'opening',
    # 'variables',
    # 'messaging',
    # 'orders',
    # 'orderreview',
    # 'billing',
    # 'mixins',
    # 'tags',
    # 'notifications',


#necessary for django allauth

    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

]


#necessary for django allauth - this will call the id of the site we are using to be attached
#to the emails we send out - eg th default is example.com
SITE_ID = 1

#necessary for django allauth
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)


# necessary for django allauth
# ACCOUNT_AUTHENTICATION_METHOD ="username" | "email" | "username_email"
ACCOUNT_AUTHENTICATION_METHOD ="username_email"
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =1
ACCOUNT_EMAIL_VERIFICATION ="mandatory"
ACCOUNT_UNIQUE_EMAIL =True
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION =True
LOGIN_REDIRECT_URL='/'


CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'teachadvisor.urls'

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

WSGI_APPLICATION = 'teachadvisor.wsgi.application'


# Database
# # https://docs.djangoproject.com/en/1.10/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# confidential
# localhost - need to install postgres under pip install and start a new database in the 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'admin',
        'PASSWORD': 'qwer1234',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_L10N = True

USE_TZ = True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

# start a folder such as the below(staticinpro/ourstatic) and dump all the static/image 
# files inside and after running the collect static the system will dump all 
# staticinpro/ourstatic files into the static_in_env/static_root and media_root
# after loading the files into staticinpro folder you dont need to run collectstatic
# but you need to use {% load staticfiles %} and "{% static 'img/marketing1.jpg' %}"
# to load the files
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static_in_pro", "our_static"),
    #os.path.join(BASE_DIR, "static_in_env"),
    #'/var/www/static/',
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "static_root")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "media_root")

# Protected has no url
PROTECTED_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "protected")
# print BASE_DIR


# confidential
#braintree payment details
BRAINTREE_PUBLIC = "2p6d25h7hnkmphkf"
BRAINTREE_PRIVATE = "dfb25d2c59f9cbf58baed0b1484a7904"
BRAINTREE_MERCHANT_ID = "366ymdm23r3gvjfh"
BRAINTREE_ENVIRONMENT = "sandbox"



# http://localhost:8000/

# http://localhost:8000/accounts/facebook/login/callback
# http://127.0.0.1:8000/accounts/facebook/login/callback

# http://127.0.0.1:8000/accounts/google/login/callback/
# http://localhost:8000/accounts/google/login/callback/

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'en_US}',
        'VERIFIED_EMAIL': True,
        'VERSION': 'v2.4'}}

SOCIALACCOUNT_PROVIDERS = \
    { 'google':
        { 'SCOPE': ['profile', 'email'],
          'AUTH_PARAMS': { 'access_type': 'online' } }}