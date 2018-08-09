# coding=utf-8

import scrapy

from ..items import DoubantvItem

class DoubantvSpider(scrapy.Spider):
    name="doubantv"
    allowed_domains = ['douban.com']
    start_urls = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=20&page_start=0"

    def parse(self, response):
        node_list = response.xpath('//*[@id="content"]/div/div[1]/div/div[4]/div')
        for node in node_list:
            item = DoubantvItem()

            item['title'] = node.xpath('./a/text()').extract_first()
            # cover
            # url
            yield item