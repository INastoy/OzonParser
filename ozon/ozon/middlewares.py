from random import randint
from time import sleep

from scrapy import signals
from scrapy.http import HtmlResponse

from ozon.services.stealth_driver import get_stealth_driver


class OzonDownloaderMiddleware:

    def __init__(self):
        self.driver = get_stealth_driver()

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)

        return s

    def process_request(self, request, spider):
        self.driver.get(request.url)
        self.driver.execute_script("window.scrollTo(5, 2000);")
        sleep(randint(2, 3))
        self.driver.delete_all_cookies()

        return HtmlResponse(request.url, encoding='utf-8', body=self.driver.page_source, request=request)

    def process_response(self, request, response, spider):

        return response

    def process_exception(self, request, exception, spider):
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

    def spider_closed(self, spider):
        self.driver.close()
        self.driver.quit()
