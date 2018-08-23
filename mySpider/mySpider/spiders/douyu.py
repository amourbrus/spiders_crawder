#coding:utf-8

import json
import scrapy
from ..items import DouyuItem
# ..表示本地文件的，不是python内的

class DouyuSpider(scrapy.Spider):

    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    base_url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    offset = 0
    start_urls = [base_url + str(offset)]
    def parse(self, response):
        data_list = json.loads(response.body)['data']  # 将json数据转为python对象

        if not data_list:
            return
        for data in data_list:
            item = DouyuItem()
            item['room_link'] = u"http://www.douyu.com/" + data['room_id']
            item['image_src'] = data['vertical_src']
            item['nick_name'] = data['nickname']
            item['city_from'] = data['anchor_city']
            yield item
            # 没有使用scrapy的pipeline的处理
            # yield scrapy.Request(item['images_src'], meta=item['nick_name'], callback=self.parse_image)

    # def parse_image(self, response):
    #     file_name = response.meta['nick_name']
    #     with open(file_name, "wb") as f:
    #         f.write(response.body)

        self.offset += 20
        yield scrapy.Request(self.base_url + str(self.offset), callback=self.parse)
