from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from ozon.spiders.smartphone_spider import PhoneSpider


def main():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(PhoneSpider)
    process.start()


if __name__ == '__main__':
    main()
