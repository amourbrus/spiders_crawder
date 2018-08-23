# -*- coding: utf-8 -*-
"""
第二版本：增加详情页：再定义一个解析函数
方式一，增加一个item类，两个文件分别存
方式二：使用同一个item类，存一个文件
"""
import json
import re


import scrapy
# 创建⼀个新的爬⾍　　scrapy genspider tencent 'tencent.com'
# from mySpider.items import TencentItem, PositionItem
from mySpider.items import TencentItem,PositionItem


class TencentSpider(scrapy.Spider):
    name = "tencent_2"
    allowed_domains = ["tencent.com"]

    base_url = 'https://hr.tencent.com/position.php?&start='
    # offset = 0
    # start_urls = [base_url + str(page) for page in range(0, 3551, 10)]
    start_urls = [base_url + str(page) for page in range(0, 101, 10)]

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
            # 版本１，同一个item，同一份文件,使用meta传item对象
            # yield scrapy.Request(item['position_link'],meta={'tencent_item':item}, callback=self.parse_position)
            # 版本２，不同文件,不同items，不同管道-加判断
            yield scrapy.Request(item['position_link'], callback=self.parse_position)
            yield item

    def parse_position(self, response):
        # item = response.meta["tencent_item"]
        item = PositionItem()

        item['position_zhize'] = response.xpath("//ul[@class='squareli']")[0].xpath("./li/text()").extract()
        item['position_yaoqiu'] = response.xpath("//ul[@class='squareli']")[1].xpath("./li/text()").extract()

        yield item  # 最后统一yield item给管道,写在同一文件












