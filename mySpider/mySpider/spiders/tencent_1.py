# -*- coding: utf-8 -*-
import re

import scrapy
# 创建⼀个新的爬⾍　　scrapy genspider tencent 'tencent.com'
from mySpider.items import TencentItem
"""第一版本，爬取所有的列表页信息

"https://hr.tencent.com/position.php?&start=" 10 3550

tr[@class='even'] | tr[@class='odd']

td[1]/a/text()
td[1]/a/@href
td[2]/text()
td[3]/text()
td[4]/text()
td[5]/text()
"""

class TencentSpider(scrapy.Spider):
    name = "tencent_1"
    allowed_domains = ["tencent.com"]

    base_url = 'https://hr.tencent.com/position.php?&start='

    offset = 0
    # start_urls = [base_url + str(offset)]  # situation 1 use offset
    # 版本３，生成所有列表页请求url，可通过列表推导式、读数据库、读本地文件等获取。
    # 适用场景：确定了总页数，可以充分利用scrapy的高并发
    start_urls = [base_url + str(page) for page in range(0,3551,10)]

    def parse(self, response):

        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for node in node_list:

            item = TencentItem()
# item取到的是unicode?
            item['position_name'] = node.xpath("./td[1]/a/text()").extract_first()
            item['position_link'] = u"https://hr.tencent.com/" + node.xpath("./td[1]/a/@href").extract_first()
            item['position_type'] = node.xpath("./td[2]/text()").extract_first()
            item['people_number'] = node.xpath("./td[3]/text()").extract_first()
            item['work_location'] = node.xpath("./td[4]/text()").extract_first()
            item['publish_times'] = node.xpath("./td[5]/text()").extract_first()

            yield item

# 第一版本
# 采用页面偏置写死了抓取的数量，网页有变动则要更改代码，另这里没法用并发。适用场景，抓取json文件：不确定总页数，也没有下一页可以点击的场景

        # if self.offset < 3550:
        #     self.offset += 10
        #     url = self.base_url + str(self.offset)
        #     yield scrapy.Request(url, callback=self.parse)

        # 第二版本，爬取所有的列表页信息使用下一页动态的获取所有页的数据；适用场景：不确定总页数；问题：和第一种一样，由于都是一个接一个的，没有充分利用到scrapy的高并发

        # if not response.xpath("//a[@class='noactive' and @id='next']"):
        #     next_link = u'https://hr.tencent.com/' + response.xpath("//a[@id='next']/@href").extract_first()
        #
        #     yield scrapy.Request(next_link, callback=self.parse)














