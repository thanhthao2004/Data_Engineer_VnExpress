# Scrapy settings for vnexpress_data_warehouse project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "vnexpress_data_warehouse"

SPIDER_MODULES = ["vnexpress_data_warehouse.spiders"]
NEWSPIDER_MODULE = "vnexpress_data_warehouse.spiders"

# Retry settings
RETRY_TIMES = 10
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}
DOWNLOAD_DELAY = 3  # Giảm tốc độ gửi yêu cầu xuống 2 giây mỗi yêu cầu
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = '/path/to/chromedriver'
SELENIUM_BROWSER_EXECUTABLE_PATH = '/path/to/google-chrome'
SELENIUM_DRIVER_ARGUMENTS = ['--headless']  # Run headless
DOWNLOAD_DELAY = 3  # Giảm tốc độ gửi yêu cầu xuống 2 giây mỗi yêu cầu
# MongoDB settings
MONGO_URI = 'mongodb://mongo:27017'
MONGO_DATABASE = 'vnexpress'

# Enable the MongoDB pipeline
ITEM_PIPELINES = {
    'vnexpress_data_warehouse.pipelines.MongoDBPipeline': 300,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "vnexpress_data_warehouse (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# DOWNLOAD_DELAY = 3

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# SPIDER_MIDDLEWARES = {
#     "vnexpress_data_warehouse.middlewares.VnexpressDataWarehouseSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# DOWNLOADER_MIDDLEWARES = {
#     "vnexpress_data_warehouse.middlewares.VnexpressDataWarehouseDownloaderMiddleware": 543,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
