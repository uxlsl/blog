"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

HOST = 'uxlsl.pythonanywhere.com'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


PROD = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7#5*=3!#8*oamaa+egc0-wn8$0dk8b%%yo&y=7^if!jq0!t%mt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [HOST]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_q',
    'bootstrap3',
    'django_extensions',
    'rest_framework',
    'rest_framework_swagger',
    'movie'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'blog.urls'

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

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if PROD:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'uxlsl$blog',
            'USER': 'uxlsl',
            'PASSWORD': '123438225',
            'HOST': 'uxlsl.mysql.pythonanywhere-services.com',
            # 'PORT': '5432',
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MOVIE_DICT = os.path.join(BASE_DIR, 'movie/movie.dict')


BOOTSTRAP3 = {
    'jquery_url': STATIC_URL + 'js/jquery.js',
    'css_url': STATIC_URL + 'css/bootstrap.min.css',
    'javascript_url': STATIC_URL + 'js/bootstrap.min.js',
}


# 定义spiders

API_KEY = '9b62163564fd4aa18707e1fa1cff4e86'
SPIDERS = [
    (31646, 'piaohua_every_day'),
]
# 最大更新数据记录保存数量
MAX_MOVIEUPDATE = 10


Q_CLUSTER = {
    'name': 'DjangORM',
    'workers': 4,
    'timeout': 90,
    'retry': 120,
    'queue_limit': 50,
    'bulk': 10,
    'orm': 'default'
}


# 邮箱配置
EMAIL_HOST = os.getenv('EMAIL_HOST', '')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')


# 日志配置

LOGDIR = os.path.join(BASE_DIR, './log')

if not os.path.exists(LOGDIR):
    os.makedirs(LOGDIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'movie': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGDIR, 'movie.log'),
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'DEBUG',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'movie': {
            'handlers': ['console', 'movie', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# 定义一些默认URL

CREATE_URL = 'http://' + HOST + '/movie/create'
MOVIE_NOTIFY_URL = 'http://' + HOST + '/movie/movie_notify/'
