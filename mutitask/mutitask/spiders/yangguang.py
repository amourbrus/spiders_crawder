# -*- coding: utf-8 -*-
import scrapy

from mutitask.items import DongguanItem


class YangguangSpider(scrapy.Spider):
    name = "yangguang"
    allowed_domains = ["wz.sun0769.com"]
    base_url = "http://wz.sun0769.com/index.php/question/questionType?type=4&page="
    offset = 0
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        # print("+"*30)
        item = DongguanItem()
        node_list = response.xpath('//*[@id="morelist"]/div/table[2]/tbody/tr/td/table/tbody/tr')

        for node in node_list:
            item["title"] = node.xpath('.//a[2][@title]/text()')
            item["number"] = node.xpath('.//td[1]/text()')
            # item["content"] = node.xpath('.//')
            item["url"] = node.xpath('.//td/a[2][@href]')
            # print(item['number'])
            yield item



