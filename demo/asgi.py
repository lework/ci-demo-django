"""
ASGI config for demo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# 设置默认的Django设置模块为新的settings包
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')

application = get_asgi_application()
