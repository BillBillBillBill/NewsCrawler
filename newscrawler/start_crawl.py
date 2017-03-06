from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from newscrawler.spiders.netease import NeteaseSpider
from newscrawler.spiders.qq import QQSpider


configure_logging()
settings = get_project_settings()
runner = CrawlerRunner(settings)


@defer.inlineCallbacks
def crawl():
    yield runner.crawl(NeteaseSpider)
    yield runner.crawl(QQSpider)
    reactor.stop()


if __name__ == '__main__':
    crawl()
    reactor.run()
