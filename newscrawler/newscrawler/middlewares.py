# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import logging
import random
from utils import redis_conn, redis_url_key, redis_invalid_url_key
from scrapy import signals
from scrapy.conf import settings
from scrapy.exceptions import IgnoreRequest
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from fake_useragent import UserAgent
from settings import USER_ANGENT_LIST
logger = logging.getLogger(__name__)


class RedisMiddleware(object):
    """
    用于去重
    """

    def process_request(self, request, spider):
        if request.url not in spider.start_urls and (redis_conn.hexists(redis_url_key, request.url) or redis_conn.hexists(redis_invalid_url_key, request.url)):
            logger.info("Skip URL: %s, has been crawled" % request.url)
            raise IgnoreRequest("URL %s has been crawled" % request.url)


class RotateUserAgentMiddleware(UserAgentMiddleware):

    def __init__(self, user_agent=''):
        self.user_agent = user_agent
        self.USER_ANGENT_LIST = USER_ANGENT_LIST

    def process_request(self, request, spider):
        random_ua = random.choice(self.USER_ANGENT_LIST)
        self.user_agent = random_ua
        request.headers.setdefault('User-Agent', random_ua)


class NewscrawlerSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
