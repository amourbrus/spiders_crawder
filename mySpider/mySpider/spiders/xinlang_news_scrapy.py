# coding=utf-8
import scrapy
from ..items import SinaItem
import os

class SinaSpider(scrapy.Spider):
    name = "sina"
    allowed_domains = ["sina.com.cn"]
    start_urls = ["http://http://news.sina.com.cn/guide/"]

    def parse(self, response):
        # ?
        # node_list = response.xpath('')
        item = SinaItem()
        item["parent_urls"] = response.xpath("//*[@id='tab01']/div/h3/a/@href").extract()
        item["parent_title"] = response.xpath("//*[@id='tab01']/div/h3/a/text()").extract()
        item["sub_urls"] = response.xpath("//*[@id='tab01']/div/ul/li/a/@href").extract()
        item["sub_title"] = response.xpath("//*[@id='tab01']/div/ul/li/a/text()").extract()
        yield item


# //*[@id="tab01"]/div/ul/li/a
#
# http://news.sina.com.cn/china/

