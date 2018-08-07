# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

# from mySpider.items import TencentItem
from mySpider.items import TencentItem,PositionItem


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class TencentJsonPipeline(object):
    def open_spider(self, spider):
        self.file = open('tencent.csv', 'w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(content.encode('utf-8'))  # py2环境，除了unicode是unicode，其他都是str，py2解释器时ascii，py3是utf-8
        return item

    def close_spider(self, spider):
        self.file.close()



# class TencentJsonPipeline(object):
#
#     def open_spider(self, spider):
#         self.file = open('tencent.json', 'w')
#
#     def process_item(self, item, spider):
#         if isinstance(item, TencentItem):
#             content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
#             self.file.write(content.encode('utf-8'))  # py2环境，除了unicode是unicode，其他都是str，py2解释器时ascii，py3是utf-8
#         return item
#
#     def close_spider(self, spider):
#         self.file.close()


# class PositionPipeline(object):
#
#     def open_spider(self, spider):
#         self.f = open('detail.json', 'w')
#
#     def process_item(self, item, spider):
#         if isinstance(item, PositionItem):
#             json_str = json.dumps(dict(item), ensure_ascii=False) + ",\n"
#             self.f.write(json_str.encode('utf-8'))
#         return item
#
#     def close_spider(self, spider):
#         self.f.close()
