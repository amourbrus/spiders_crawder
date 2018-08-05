# -*- coding: utf-8 -*-
import re

import scrapy
# 创建⼀个新的爬⾍　　scrapy genspider tencent 'tencent.com'
from mySpider.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["tencent.com"]
    # start_urls = (
    #     'https://hr.tencent.com/position.php?&start=',
    # )

    base_url = 'https://hr.tencent.com/position.php?&start='

    offset = 0
    start_urls = [base_url + str(offset)]  # situation 1 use offset
    # start_urls = [base_url + str(page) for page in range(0, 3551, 10)]

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

        if self.offset < 3550:
            self.offset += 10
            url = self.base_url + str(self.offset)
            yield scrapy.Request(url, callback=self.parse)



            # yield scrapy.Request(url, callback=self.parse)

            # yield item












