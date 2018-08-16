# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class MutitaskPipeline(object):
    def process_item(self, item, spider):
        return item


class TencentJsonPipeline(object):

    def __init__(self):
        self.file = open('tecent.json', 'w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False) + ",\n"
        self.file.write(content.encode('utf8'))  # 文件显示的是中文
        return item

    def close_spider(self, spider):
        self.file.close()

