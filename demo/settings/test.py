from .base import *

# 使用与开发环境相同的密钥，但在实际项目中应该为每个环境使用不同的密钥
SECRET_KEY = 'django-insecure-test-y)^a7cta!dbsng&+g_snp7o3n^q^)i(obcg0k714pv^8'

# 测试环境通常仍然开启调试
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# 测试环境可能使用不同的数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 测试环境特有的设置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'application.log',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
} 