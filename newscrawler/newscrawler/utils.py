# coding: utf-8
import redis
from scrapy.conf import settings


redis_conn = redis.Redis(
    host=settings['REDIS_CONF']['host'],
    port=settings['REDIS_CONF']['port'],
    db=settings['REDIS_CONF']['db']
)
redis_url_key = "url"
