# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from lib import db_utils
import mongoengine as m

db_utils.using_db("news")


class NewsItem(m.Document):
    title = m.StringField()
    content = m.StringField()
    source = m.StringField()
    published = m.DateTimeField()
    url = m.StringField()

    meta = {
        'db_alias': 'news',
        'collection': 'news',
    }

    def to_json(self):
        return {
            'title': self.title,
            'content': self.content,
            'source': self.source,
            'published': self.published,
            'url': self.url,
        }


class Subscription(m.Document):
    open_id = m.StringField()
    keywords = m.ListField(m.StringField())  # 关键词
    tags = m.ListField(m.StringField())  # 标签

    meta = {
        'db_alias': 'news',
        'collection': 'subscription',
    }

    @staticmethod
    def ensure_subscription(open_id):
        subscription = Subscription.objects(open_id=open_id).first()
        if not subscription:
            subscription = Subscription(open_id=open_id)
            subscription.save()
        return subscription

    @staticmethod
    def add_keyword(open_id, keyword):
        subscription = Subscription.ensure_subscription(open_id)
        subscription.update(add_to_set__keywords=keyword)

    @staticmethod
    def remove_keyword(open_id, keyword):
        subscription = Subscription.ensure_subscription(open_id)
        subscription.update(pull__keywords=keyword)

    def to_json(self):
        return {
            'open_id': self.open_id,
            'keywords': self.keywords,
            'tags': self.tags
        }
