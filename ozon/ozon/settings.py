BOT_NAME = 'ozon'

SPIDER_MODULES = ['ozon.spiders']
NEWSPIDER_MODULE = 'ozon.spiders'

LOG_LEVEL = 'INFO'

ROBOTSTXT_OBEY = False
DOWNLOADER_MIDDLEWARES = {
   'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
   'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
   'ozon.middlewares.OzonDownloaderMiddleware': 800,
}

# Free Proxy
ROTATING_PROXY_LIST = [
   '208.82.61.66:3128', '159.89.228.253:38172', '208.82.61.38:3128', '165.225.38.91:10605', '104.129.204.254:10729',
   '192.53.121.174:3128', '104.129.205.49:10605', '208.82.61.13:3128', '143.198.72.194:3128', '165.225.56.55:10605',
   '208.82.61.12:3128', '20.112.216.211:3128', '54.86.198.153:80', '20.112.217.31:3128', '51.222.13.193:10084',
   '167.114.173.66:53040', '165.225.216.114:10605', '165.225.38.76:10605', '104.148.36.10:80', '208.82.61.31:3128',
   '5.161.156.151:3000', '5.161.90.204:3128', '47.89.185.178:8888', '165.225.38.97:10605', '68.183.131.244:8081',
   '142.44.241.192:7497', '51.222.12.245:10084', '143.198.187.65:38172', '205.207.101.177:8282', '165.225.8.109:10605',
   '64.40.228.50:80', '165.225.208.100:10605', '44.229.129.178:3128', '44.206.211.16:80', '178.128.156.76:443',
   '3.220.186.248:80', '18.234.161.107:3128'
]
ROTATING_PROXY_LOGSTATS_INTERVAL = 15

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 4
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'ozon.middlewares.OzonSpiderMiddleware': 543,
# }


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'ozon.pipelines.OzonPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
