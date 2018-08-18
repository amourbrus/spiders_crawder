# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
# from mySpider.items import TencentItem
import scrapy
from mySpider.items import TencentItem,PositionItem
from scrapy.pipelines.images import ImagesPipeline
from settings import IMAGES_STORE
import logging

class MyspiderPipeline(object):
    def process_item(self, item, spider):
        return item

# class SinaPipeline(object):
#     def process_item[]



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

class DouyuImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 发送每个图片的请求，默认图片保存在settings,py中的IMAGES_STORE指定路径下
        yield scrapy.Request(item['image_src'])

    def item_completed(self, results, item, info):
        # print("----"*20,results)
        # return item
        results_path = [x['path'] for ok, x in results if ok][0]
        # 源文件绝对路径， pwd --- IMAGES_STORE
        old_name = IMAGES_STORE + results_path
        new_name = IMAGES_STORE + item['nick_name'] + ".jpg"
        try:
            os.rename(old_name, new_name)
        except Exception as e:
            logging.error(e)

        return item

# results = [
#     (   True,
#         {'url': 'https://rpic.douyucdn.cn/live-cover/appCovers/2018/06/02/1264973_20180602141527_big.jpg',
            # 'path': 'full/be2c9b584a51acfcef4d2dae1d169a38b01f2ab1.jpg',
            # 'checksum': 'd95281e0b865baa916d648cdf910cbea'}
#      )
# ]


# 13家哦公司网站，日100w， redis、scrapy  -- app，新闻
# 航班信息 --- 协程等旅游使用
# 维护 -- 写的爬虫稳定
# 细节过滤
