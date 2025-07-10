import os

# 默认使用开发环境
env = os.environ.get('APP_ENV', 'dev')

if env == 'prod':
    from .prod import *
elif env == 'test':
    from .test import *
else:
    from .dev import * 