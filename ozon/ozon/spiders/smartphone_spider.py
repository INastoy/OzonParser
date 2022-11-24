import logging
import re

import pandas as pd
import scrapy
from scrapy import signals
from scrapy.http import HtmlResponse

logger = logging.getLogger(__name__)

REQUIRED_QUANTITY = 100


class PhoneSpider(scrapy.Spider):

    phone_urls = []
    os_versions = []
    count = 0

    name = 'phone_spider'
    start_urls = ['https://www.ozon.ru/category/telefony-i-smart-chasy-15501/?sorting=rating']

    def parse(self, response: HtmlResponse, **kwargs):
        urls = response.css('div.s4k div.k6s a::attr(href)').extract()
        for url in urls:
            if url.startswith('/product/smartfon'):
                cleaned_url = url.split('?')[0]
                self.phone_urls.append(cleaned_url)

        next_page = response.css('div.aam9 a::attr(href)').get()
        if len(self.phone_urls) < REQUIRED_QUANTITY and next_page:
            yield response.follow(next_page, callback=self.parse)

        else:
            for url in self.phone_urls[:REQUIRED_QUANTITY]:

                yield response.follow(url, callback=self.parse_phone, dont_filter=True)

    def parse_phone(self, response: HtmlResponse, **kwargs):
        os_version = response.xpath('//dt[span[contains(text(), "Версия")]]/following-sibling::dd').css('::text').get()
        self.count += 1
        logger.info(f'{self.count}/{REQUIRED_QUANTITY}')

        if not os_version:
            os_version = 'Версия ОС не указана'
        elif 'Android' in os_version:
            os_version = re.match(r'Android \d{1,2}', os_version).group()

        logger.info(f'Crawled URL: {response.url}')
        logger.info(f'Crawled OS: {os_version}')

        self.os_versions.append(os_version)

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(PhoneSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)

        return spider

    def spider_closed(self, spider):
        result = pd.Series(self.os_versions).value_counts()
        logger.info('Сбор завершен')
        logger.info(f'Results:\n{result}')
