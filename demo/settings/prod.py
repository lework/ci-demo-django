from .base import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
# 在生产环境中，应从环境变量获取SECRET_KEY
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-y)^a7cta!dbsng&+g_snp7o3n^q^)i(obcg0k714pv^8nni9i_')

# 生产环境关闭调试
DEBUG = False

# 允许的主机列表，根据实际情况配置
ALLOWED_HOSTS = ['*']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 生产环境日志设置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'application.log',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'WARNING',
    },
}

# 静态文件设置
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage' 