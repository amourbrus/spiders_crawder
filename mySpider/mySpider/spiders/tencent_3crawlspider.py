# -*- coding: utf-8 -*-
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












