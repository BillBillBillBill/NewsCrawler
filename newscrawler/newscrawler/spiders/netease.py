# -*- coding: utf-8 -*-
import scrapy
import re
import time
from datetime import datetime
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.shell import inspect_response
from newscrawler.items import NewsItem


class NeteaseSpider(CrawlSpider):
    name = "netease"
    allowed_domains = ["163.com"]
    start_urls = ['http://tech.163.com/']

    rules = (
        Rule(LinkExtractor(allow=('/\d+/\d+/\d+/*', )), callback='parse_item'),
    )

    def parse_item(self, response):
        # inspect_response(response, self)
        r = response
        title = r.xpath('/html/head/title/text()').extract()[0].strip()
        source = r.xpath("//a[@id='ne_article_source']/text()").extract()[0].strip()
        content = "".join(r.xpath("//div[@id='endText']/p/text()").extract()).strip()
        raw_time = r.xpath("//div[@class='post_time_source']/text()").extract()[0]
        re_result = re.findall("\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", raw_time)
        if re_result:
            ts = time.mktime(time.strptime(re_result[0], '%Y-%m-%d %H:%M:%S'))
        else:
            ts = 0
        url = r.url
        new_news = NewsItem(
            title=title,
            content=content,
            source=source,
            published=ts,
            url=url
        )
        return new_news
