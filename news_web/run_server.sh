#!/bin/bash
echo "启动服务器"
#python manage.py runserver 0.0.0.0:8000
gunicorn news_web.wsgi:application -w 4 -b :8000 -k gevent --max-requests 1000
