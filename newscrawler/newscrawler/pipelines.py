# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import logging
from utils import redis_conn, redis_url_key
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from wechat_push import send_msg
logger = logging.getLogger(__name__)


class MongoDBPipeline(object):

    def __init__(self):
        conn = pymongo.Connection(
            settings['MONGO_CONF']['host'],
            settings['MONGO_CONF']['port']
        )
        db = conn[settings['MONGO_CONF']['db']]
        self.news_collection = db[settings['MONGO_CONF']['collection']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.news_collection.insert(dict(item))
            logger.info("Question added to MongoDB database!")
        return item


class RedisPipeline(object):

    def process_item(self, item, spider):
        redis_conn.hset(redis_url_key, item['url'], 0)
        return item


class PushPipeline(object):

    def process_item(self, item, spider):
        send_msg(title=item['title'], data=item['content'])
        return item
