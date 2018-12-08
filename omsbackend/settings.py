# -*- coding:utf-8 -*-
"""
Django settings for omsbackend project.

Generated by 'django-admin startproject' using Django 1.10.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import sys
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&pi^9b1=sa%u%*&mguhufzk@kt7vv4v3dp)#s038j!lfxv^rna'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'salt',
    'rest_framework',
    'assets',
    'cloud',
    'channels',     #websocket
    'corsheaders',  #跨域
    'xadmin',
    'crispy_forms',
    'reversion',
    'django_filters',  # 过滤

]


#跨域访问安装django-cors—headers，并配置MIDDLEWARE
CORS_ORIGIN_ALLOW_ALL = True

AUTH_USER_MODEL = "users.UserProfile"

AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',

)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'omsbackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'dist')]
        ,
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

WSGI_APPLICATION = 'omsbackend.wsgi.application'

#手机号码正则表达式
REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "dist/static"),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


REST_FRAMEWORK = {

    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser'
    )
}
#JWT相关设置
import datetime
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}


# salt-api地址
SALT_API_URL = 'https://192.168.55.128:8000'
# salt-api用户
SALT_API_NAME = 'saltapi'
# salt-api密码
SALT_API_PWD = '123456'
# salt服务端安装的minion的id，服务端也要安装一下minion，有很多用到的时候
SALT_MASTER = '192.168.55.128'
# salt服务端IP，salt-ssh等调用
SALT_MASTER_IP = '192.168.55.128'
#LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}  # 日志格式
    },
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
            },
        # 下面是django自带的最详细的输出
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/all.log'),     # 日志输出文件，根目录下需要手动新建
            'maxBytes': 1024*1024*5,                  # 文件大小5M
            'backupCount': 5,                         # 备份份数
            'formatter': 'standard',                   # 使用哪种formatters日志格式上面定义了standard
        },
        # 下面是django自带的控制台输出
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        # 下面是django自带的5xx或者4xx错误记录在script.log里
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/script.log'),
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter': 'standard',
            },
        # 下面是django自带的脚本错误记录
        'scprits_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR,'logs/script.log'),
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter': 'standard',
            }
    },
    # 下面是定义日志器
    'loggers': {

        'django': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },

        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False,  # 是否继承父类
            },
        'scripts': {
            'handlers': ['scprits_handler'],
            'level': 'INFO',
            'propagate': False
        },
        # 下面是给views调用使用的
        'oms.views': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}


# Channels
ASGI_APPLICATION = 'omsbackend.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

#TencentApi
from . import config
SECRETID = config.SECRETID
SECRETKEY = config.SECRETKEY