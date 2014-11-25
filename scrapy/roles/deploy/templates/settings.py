# -*- coding:utf-8 -*-

# Scrapy settings for zhihu project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'zhihu'

# USERNAME = 'cml_hawke0@163.com'
# PASSWORD = '56121353'

USERNAME = 'yyluo_sep.27@hotmail.com'
PASSWORD = 'damiyy66526844'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'

LOG_FILE = 'zhihu.log'
LOG_LEVEL= 'DEBUG'

SCHEDULER_ORDER = 'BFO'

RETRY_ENABLED = False

CONCURRENT_ITEMS = 100
CONCURRENT_REQUESTS = 1

DNSCACHE_ENABLED = True
#DUPEFILTER_CLASS = 'scr'

COOKIES_DEBUG = False

DOWNLOAD_DELAY = 1
DOWNLOAD_TIMEOUT = 15
RANDOMIZE_DOWNLOAD_DELAY = True


# Enables scheduling storing requests queue in redis.
#SCHEDULER = "zhihu.scrapy_redis.scheduler.Scheduler"
SCHEDULER = "zhihu.scrapy_redis.nscheduler.Scheduler"

# Don't cleanup redis queues, allows to pause/resume crawls.
SCHEDULER_PERSIST = True

# Schedule requests using a priority queue. (default)
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

# Schedule requests using a queue (FIFO).
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'

# Schedule requests using a stack (LIFO).
#SCHEDULER_QUEUE_CLASS = 'zhihu.scrapy_redis.queue.SpiderStack'
SCHEDULER_QUEUE_CLASS = 'zhihu.scrapy_redis.nqueue.SpiderQueue'

# Max idle time to prevent the spider from being closed when distributed crawling.
# This only works if queue class is SpiderQueue or SpiderStack,
# and may also block the same time when your spider start at the first time (because the queue is empty).
SCHEDULER_IDLE_BEFORE_CLOSE = 10

ITEM_PIPELINES = {
    #'zhihu.pipelines.DoNothingPipeline': 300,
    #'zhihu.pipelines.JsonWithEncodingPipeline': 300,
#    'scrapy_redis.pipelines.RedisPipeline':200,
    'zhihu.pipelines.MongoDBPipeline': 300,
    }

DOWNLOADER_MIDDLEWARES = {
    # 'zhihu.misc.middleware.CustomHttpProxyMiddleware': 543,
    'zhihu.misc.middleware.CustomUserAgentMiddleware': 545,
    }
# Specify the host and port to use when connecting to Redis (optional).
#REDIS_HOST = 'localhost'
#REDIS_PORT = 6379

MONGO_HOST = '{{ MONGO_HOST }}'
MONGO_PORT = {{ MONGO_PORT }}
MONGO_USER = '{{ MONGO_USER }}'
MONGO_PASSWORD = '{{ MONGO_PASSWORD }}'
QUEUE_HOST = '106.185.44.133'
QUEUE_PORT = 10086 



# HEADER={
#     "Host": "www.zhihu.com",
#     "Connection": "keep-alive",
#     "Cache-Control": "max-age=0",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36",
#     "Referer": "http://www.zhihu.com/people/raymond-wang",
#     "Accept-Encoding": "gzip,deflate,sdch",
#     "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2",
#     }
#
# COOKIES={
#     'checkcode':r'"$2a$10$9FVE.1nXJKq/F.nH62OhCevrCqs4skby2bC4IO6VPJITlc7Sh.NZa"',
#     'c_c':r'd871da9047a411e48d855254291c3363',
#     # '_ga':r'GA1.2.1063404131.1384259893',
#     # 'zata':r'zhihu.com.021715f934634a988abbd3f1f7f31f37.470330',
#     'q_c1':r'6390f6f8ec0a4023ba3a0ee5a9d52cd6|1411973343000|1411973343000',
#     '_xsrf':r'384d87bb70ba4af04cdd16d5fd326cf6',
#     'q_c0':r'"NDI4ZDg1ZWMzN2NlMTFmZTM4MDRmYzJjMjkxMDU4YmR8S0JZdzU3cldCTGFmZ2Zhdg==|1411973413|85a2cc5cea3465bd2a24c2d65ce73dd3459e01de"',
#     '__utma':r'51854390.1199979180.1413359208.1413540845.1413780932.13',
#     '__utmb':r'51854390.4.10.1400522270',
#     '__utmc':r'51854390',
#     '__utmz':r'51854390.1413540845.12.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
#     '__utmv':r'51854390.100-1|2=registration_date=20121104=1^3=entry_date=20121104=1'
# }

