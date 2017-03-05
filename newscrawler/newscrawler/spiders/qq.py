# -*- coding: utf-8 -*-
import scrapy
import re
import time
from datetime import datetime
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.shell import inspect_response
from newscrawler.items import NewsItem


class QQSpider(CrawlSpider):
    name = "qq"
    allowed_domains = ["tech.qq.com"]
    start_urls = ['http://tech.qq.com/']

    rules = (
        Rule(LinkExtractor(allow=('http://tech.qq.com/a/\d+/*', )), callback='parse_item'),
    )

    def parse_item(self, response):
        r = response
        # inspect_response(response, self)
        title = r.xpath("//div[@class='qq_article']//h1/text()").extract()[0]
        # title = response.xpath("//div[@id='C-Main-Article-QQ']//h1/text()").extract()[0]
        source = r.xpath("//div[@class='qq_article']//span[@class='a_source']/text()").extract()[0]
        content = ''.join(r.xpath('//div[@id="Cnt-Main-Article-QQ"]/p/text()').extract())
        raw_time = r.xpath("//div[@class='qq_article']//span[@class='a_time']/text()").extract()[0]
        re_result = re.findall("\d{4}-\d{2}-\d{2} \d{2}:\d{2}", raw_time)
        if re_result:
            ts = time.mktime(time.strptime(re_result[0], '%Y-%m-%d %H:%M'))
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
