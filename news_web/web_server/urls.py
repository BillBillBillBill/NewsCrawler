# coding: utf-8
from django.conf.urls import url
from views import ping, news, subscriptions

urlpatterns = [
    url(r'^ping$', ping),
    url(r'^news$', news),
    url(r'^subscriptions$', subscriptions),
]
