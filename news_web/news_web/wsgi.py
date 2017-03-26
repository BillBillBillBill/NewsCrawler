"""
WSGI config for news_web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
from gevent import monkey
from django.core.wsgi import get_wsgi_application


monkey.patch_all()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_web.settings")

application = get_wsgi_application()
