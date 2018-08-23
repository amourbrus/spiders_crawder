# 小案例，爬取hr_tencent

> 版本1：**爬取所有详情页**

```python
# item.python
import scrapy

class TencentItem(scrapy.Item):
    position_name = scrapy.Field()
    position_link = scrapy.Field()
    position_type = scrapy.Field()
    people_number = scrapy.Field()
    work_location = scrapy.Field()
    publish_times = scrapy.Field()

# tencent.py
import scrapy
from mySpider.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    base_url = 'https://hr.tencent.com/position.php?&start='
    offset = 0
    # start_urls = [base_url + str(offset)]
    # 方式3生成所有列表页请求url，可通过列表推导式、读数据库、读本地文件等获取。
    # 适用场景：确定了总页数，可以充分利用scrapy的高并发
    start_urls = [base_url + str(page) for page in range(0,3551,10)]

    def parse(self, response):
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for node in node_list:
            item = TencentItem()
            item['position_name'] = node.xpath("./td[1]/a/text()").extract_first()
            item['position_link'] = u"https://hr.tencent.com/" + node.xpath("./td[1]/a/href").extract_first()
            item['position_type'] = node.xpath("./td[2]/a/text()").extract_first()
            item['people_number'] = node.xpath("./td[3]/a/text()").extract_first()
            item['work_location'] = node.xpath("./td[4]/a/text()").extract_first()
            item['publish_times'] = node.xpath("./td[5]/a/text()").extract_first()
            yield item
        # 方式1采用页面偏置写死了抓取的数量，网页有变动则要更改代码，另这里没法用并发。适用场景，抓取json文件：不确定总页数，也没有下一页可以点击的场景
        # if self.offset < 3550:
        #     self.offset += 50
        #     url = self.base_url() + str(self.offset)
        #     yield scrapy.Request(url, callback=self.parse)

        # 方式2 爬取所有的列表页信息使用下一页动态的获取所有页的数据；适用场景：不确定总页数；问题：和第一种一样，由于都是一个接一个的，没有充分利用到scrapy的高并发
        # if not response.xpath("//a[@class='noactive' and @id='next']"):
        #     next_link = u'https://hr.tencent.com/' + response.xpath("//a[@id='next']/@href").extract_first()
        #
        #     yield scrapy.Request(next_link, callback=self.parse)

```
```python
# pipelines.py
import json
from mySpider.items import TencentItem, PositionItem
class TencentJsonPipeline(object):
    def open_spider(self, spider):
        self.file = open('tencent.json', 'w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(content.encode('utf-8'))
        return item
    def close_spider(self,spider):
        self.file.close()

```

> 版本2 **爬取包含详情页**

### 方案一，保存在同一份文件,使用同一个item类

```python
# items.py
class TencentItem(scrapy.Item):
    # 职位名
    position_name = scrapy.Field()
    # 职位详情链接
    position_link = scrapy.Field()
    # 职位类别
    position_type = scrapy.Field()
    # 招聘人数
    people_number = scrapy.Field()
    # 工作地点
    work_location = scrapy.Field()
    # 发布时间
    publish_times = scrapy.Field()

    position_zhize = scrapy.Field()
    position_yaoqiu = scrapy.Field()

# tencent.py
class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    base_url = 'https://hr.tencent.com/position.php?&start='
    start_urls = [base_url + str(page) for page in range(0, 3551, 10)]
    def parse(self, response):
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for node in node_list:
            item = TencentItem()
            item['position_name'] = node.xpath("./td[1]/a/text()").extract_first()
            item['position_link'] = u"https://hr.tencent.com/" + node.xpath("./td[1]/a/@href").extract_first()
            item['position_type'] = node.xpath("./td[2]/text()").extract_first()
            item['people_number'] = node.xpath("./td[3]/text()").extract_first()
            item['work_location'] = node.xpath("./td[4]/text()").extract_first()
            item['publish_times'] = node.xpath("./td[5]/text()").extract_first()

            yield scrapy.Request(item['position_link'], meta={'tencent_item':item}, callback=self.parse_position)

    def parse_position(self, response):
        item = response.meta['tencent_item']
        item['position_zhize'] = response.xpath("//ul[@class='squareli']")[0].xpath("./li/text()").extract()
        item['position_yaoqiu'] = response.xpath("//ul[@class='squareli']")[1].xpath("./li/text()").extract()

        yield item
```

### 方案二，保存在两份文件
- 需要建一个item类，不同的对象
- 需要再建一个管道，然后判断item对象来自哪个item类分别处理 isinstance
- 注意：没有出现详情文件是因为：没有在setting中设置管道

```python
# 修改items.py 新增一个类

class PositionItem(scrapy.Item):
    position_zhize = scrapy.Field()
    position_yaoqiu = scrapy.Field()

# tencent.py
# 修改yield
        yield scrapy.Request(item['position_link'], callback=self.parse_position)
        yield item

def parse_position(self, response):
    item = PositionItem()

    item['position_zhize'] = response.xpath("//ul[@class='squareli']")[0].xpath("./li/text()").extract()
    item['position_yaoqiu'] = response.xpath("//ul[@class='squareli']")[1].xpath("./li/text()").extract()

    yield item

# pipelines.py
# item对象会经过所有的管道，所以加判断
def process_item(self, item, spider):
    if isinstance(item, TencentItem):
        content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(content.encode('utf-8'))
    return item

# 同理，修改 PositionPipelien 的process_item
```

# CrawlSpiders

> **使用CrawlSpider- 增加rule用来自动发送linkextractors提取的url**

唯一改变的就是tencent.py 而且也几乎只增了rules,缺点- **只能存在多个文件中**
适合只取详情页数据

 *CrawSpider 是爬虫类,Rule发送LinkExtractor提取的链接请求，并根据callback和folllow处理*
*提取符合正则匹配规则的链接，并自动发送请求
    返回的响应，交给callback指定的回调函数解析
       1. follow=True，表示响应还会交给rules继续提取新的链接并发送请求返回响应，
       2  follow=False, 表示响应只交给callback回调函数解析，不再继续提取新*

```python
# tencent.py
"""
使用CrawlSpider- 增加rule用来自动发送linkextractors提取的url
"""


# CrawSpider 是爬虫类,Rule发送LinkExtractor提取的链接请求，并根据callback和folllow处理
from scrapy.spiders import CrawlSpider, Rule

# 链接提取器
from scrapy.linkextractors import LinkExtractor

from mySpider.items import TencentItem,PositionItem


class TencentSpider(CrawlSpider):
    name = "tencent_crawl"
    allowed_domains = ["tencent.com"]
    # 只需要一个start_urls就ｏｋ
    start_urls = ["https://hr.tencent.com/position.php?&start=0"]

    # 提取符合正则匹配规则的链接，并自动发送请求
    # 返回的响应，交给callback指定的回调函数解析
    #   1. follow=True，表示响应还会交给rules继续提取新的链接并发送请求返回响应，
    #   2  follow=False, 表示响应只交给callback回调函数解析，不再继续提取新连接
    rules = [
        Rule(LinkExtractor(allow=r"position\.php\?&start=\d+"), callback="parse_page", follow=True),
        Rule(LinkExtractor(allow=r"position_detail\.php\?id=\d+"), callback="parse_position", follow=False)

    ]
    # 一定不能是parse
    def parse_page(self, response):

        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for node in node_list:

            item = TencentItem()
            item['position_name'] = node.xpath("./td[1]/a/text()").extract_first()
            item['position_link'] = u"https://hr.tencent.com/" + node.xpath("./td[1]/a/@href").extract_first()
            item['position_type'] = node.xpath("./td[2]/text()").extract_first()
            item['people_number'] = node.xpath("./td[3]/text()").extract_first()
            item['work_location'] = node.xpath("./td[4]/text()").extract_first()
            item['publish_times'] = node.xpath("./td[5]/text()").extract_first()

            # 不再需要手动发请求
            yield item

    def parse_position(self, response):
        # item = response.meta["tencent_item"]
        item = PositionItem()

        item['position_zhize'] = response.xpath("//ul[@class='squareli']")[0].xpath("./li/text()").extract()
        item['position_yaoqiu'] = response.xpath("//ul[@class='squareli']")[1].xpath("./li/text()").extract()

        yield item

```


```python
# mongodb存储
from scrapy.conf import settings
import pymongo

class DoubanspiderPipeline(object):
    def __init__(self):
        # 获取setting主机名、端口名和数据库名
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']

        client = pymongo.MongoClient(host=host, port=port)

        mdb = client[dbname]
        self.post = mdb[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item

```
### 导出csv、存储数据到csv


### 模拟登录
* 直接发送cookies
* 发送账号和密码

```python
#coding:utf-8
# 发送账号和密码

import scrapy


class RenrenSpider(scrapy.Spider):
    name = "renren_login_post"
    allowed_domains = ['renren.com']
    #start_urls = [""]


    def start_requests(self):
        """
            发送登录页面的post请求，登录成功后，Scrapy会记录Cookie
        """
        post_url = "http://www.renren.com/PLogin.do"

        formdata = {
            "email" : "mr_mao_hacker@163.com",
            "password" : "alarmchime"
        }

        #scrapy.Request(url)
        yield scrapy.FormRequest(post_url, formdata=formdata, callback=self.parse)


    def parse(self, response):
        """
            附带Cookie 发送其他页面的get请求，获取页面数据
        """
        url_list = [
            "http://www.renren.com/410043129/profile",
            "http://www.renren.com/965999739/profile"
        ]

        for url in url_list:
            yield scrapy.Request(url,callback = self.parse_page)


    def parse_page(self, response):
        """
            提取页面数据做后续处理
        """
        file_name = response.xpath("//title/text()").extract_first()

        with open(file_name, "w") as f:
            f.write(response.body)


```
```python
#coding:utf-8
# 发送cookies

import scrapy

class RenrenSpider(scrapy.Spider):
    name = "renren_cookies"
    allowed_domains = ["renren.com"]
    start_urls =[
        "http://www.renren.com/410043129/profile",
        "http://www.renren.com/965999739/profile"
    ]

    def start_requests(self):
        cookies = {"anonymid" : "j7wsz80ibwp8x3",
            "_r01_" : "1",
            "ln_uact" : "mr_mao_hacker@163.com",
            "depovince" : "GW",
            "ick_login" : "a50cbea9-3d00-4458-9665-54c6e9557743",
            "first_login_flag" : "1",
            "loginfrom" : "syshome",
            "wp_fold" : "0",
            "JSESSIONID" : "abcXIDq6u5j8b4XKdusuw",
            "_de" : "BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5",
            "id" : "327550029",
            "jebecookies" : "57c3105e-6e27-45b1-a529-38026372c50d|||||",
            "p" : "36a01dc1e912bd6932a15f60174b60be9",
            "ln_hurl" : "http://hdn.xnimg.cn/photos/hdn121/20180807/1115/main_WKP9_0ab200000ea5195a.jpg",
            "t" : "a53991a23060e9ec4810b9515d82d1509",
            "societyguester" : "a53991a23060e9ec4810b9515d82d1509",
            "xnsid" : "ed9988de"
        }

        headers = {
            "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding" : "gzip, deflate",
            "Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control" : "max-age=0",
            "Connection" : "keep-alive",
            "Host" : "www.renren.com",
            "Upgrade-Insecure-Requests" : "1",
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }

        for url in self.start_urls:
            # scrapy的cookie可以动态传递,注意单独传cookies参数
            yield scrapy.Request(url, cookies=cookies, headers=headers, callback=self.parse_page)

    def parse_page(self, response):
        """
            提取页面数据做后续处理
        """
        file_name = response.xpath("//title/text()").extract_first()

        with open(file_name, "w") as f:
            f.write(response.body)

```

### 下载中间件
middlewares.py
```python

# -*- coding: utf-8 -*-

import random

from settings import USER_AGENT_LIST

import logging



class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        #scrapy.Request()
        # scrapy.FromRequest()

        # 每个请求下载前，都会经过下载中间件的process_request进行预处理
        # 可以给每个请求更换一个新的User-Agent
        user_agent = random.choice(USER_AGENT_LIST)
        request.headers["User-Agent"] = user_agent
        # print("--" * 50)
        # print(request.headers)


        #logging.warning("--" * 50)
        #logging.warning(request.headers)

        spider.logger.debug("--" * 50)
        spider.logger.warning("--" * 50)


        # 早期scrapy日志使用方式
        # from scrapy import log
        #log.msg("Hello world!", level='log.INFO')

        # 主要不要return request给引擎，不然引擎会认为是下载失败的请求，会重新加入调度器请求队列


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        # 免费代理的格式
        #proxy = "http://115.28.141.184:16816"
        # 验证代理的格式
        proxy = "http://maozhaojun:ntkn0npx@115.28.141.184:16816"

        # scrapy的request对象提供了meta字典的proxy键来存储代理信息
        request.meta["proxy"] = proxy



```
