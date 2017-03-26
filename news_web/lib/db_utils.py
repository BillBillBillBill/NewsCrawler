# -*- coding: utf-8 -*-
import time
import datetime
import mongoengine


def now():
    return datetime.datetime.utcnow()


def get_utc_seconds(dt):
    return int(time.mktime(dt.timetuple()) - time.timezone)


def using_db(alias):
    mongoengine.register_connection(
        alias, alias,
        host="localhost",
        port=27017
    )
