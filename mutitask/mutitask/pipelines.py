# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json


class MutitaskPipeline(object):
    def process_item(self, item, spider):
        return item


class TencentJsonPipeline(object):

    def __init__(self):
        # 方式一打开文件
        self.file = open('tecent.json', 'w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False) + ",\n"
        self.file.write(content.encode('utf8'))  # 文件显示的是中文
        # 使用 scrapy crawl itcast -o teachers.json 显示的是unicode
        # py2环境
        return item

    def close_spider(self, spider):
        self.file.close()

class YangguangJsonPipeline(object):

    def __init__(self):
        # 方式二打开文件
        self.file = codecs.open('dongguan.json','w',encoding='utf-8')

    # def process_item(self, item, spider):
        # content = json.dumps(dict(item), ensure_ascii=False)
        # self.file.write(content)
        # return item

    def spider_closed(self, spider):
        self.file.close()


class DoubanJsonPipeline(object):

    def __init__(self):
        self.file = open('yichuhaoxi.json','w')

    def spider_close(self,spider):
        self.file.close()

    def process_item(self, item, spider):
        print("="*50)
        content = json.dumps(dict(item),ensure_ascii=False)
        self.file.write(content.encode('utf-8'))
        return item




