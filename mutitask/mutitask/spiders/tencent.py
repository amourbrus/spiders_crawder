# -*- coding: utf-8 -*-
import re

import scrapy

# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

from mutitask.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["tencent.com"]
    start_urls = (
        'http://hr.tencent.com/position.php?&start=0#a',
    )
    # start_urls = ["http://www.itcast.cn/channel/teacher.shtml"]


    def parse(self, response):

        # with open('file.html', 'w') as f:
        #     f.write(response.text.encode('utf8'))
        # 提取列表页信息
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for node in node_list:
            item = TencentItem()
            item['name'] = node.xpath('./td[1]/a/text()').extract_first()
            item['detailLink'] = node.xpath('./td[1]/a/@href').extract_first()
            item['positionInfo'] = node.xpath('./td[2]/a/text()').extract_first()
            item['peopleNumber'] = node.xpath('./td[3]/a/text()').extract_first()
            item['workLocation'] = node.xpath('./td[4]/a/text()').extract_first()
            item['publishTime'] = node.xpath('./td[5]/a/text()').extract_first()

            # 下一页 === 采用url方法
            currentPage = re.search('(\d+)',response.url).group(1)
            page = int(currentPage) + 10
            url = re.sub('\d+', str(page), response.url)

            yield scrapy.Request(url, callback=self.parse)

            yield item



