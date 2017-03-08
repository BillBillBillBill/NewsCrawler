# coding: utf-8
from django.conf.urls import url
from views import ping, news

urlpatterns = [
    url(r'^ping$', ping),
    url(r'^news$', news),
]
