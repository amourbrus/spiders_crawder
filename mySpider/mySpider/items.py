# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ItcastItem(scrapy.Item):
    name = scrapy.Field()
    level = scrapy.Field()
    info = scrapy.Field()

class TencentItem(scrapy.Item):
    # 职位名
    position_name = scrapy.Field()
    # 职位详情链接
    position_link = scrapy.Field()
    # 职位类别
    position_type = scrapy.Field()
    # 招聘人数
    people_number = scrapy.Field()
    # 工作地点
    work_location = scrapy.Field()
    # 发布时间
    publish_times = scrapy.Field()


class PositionItem(scrapy.Item):
    position_zhize = scrapy.Field()
    position_yaoqiu = scrapy.Field()


import sys

reload(sys)
# sys.setdefaultencoding("utf-8")
# 系统设置编码

class SinaItem(scrapy.Item):
    # 大类的标题和url
    parent_title = scrapy.Field()
    parent_urls = scrapy.Field()
    # 小类的标题和子url
    sub_title = scrapy.Field()
    sub_urls = scrapy.Field()

    sub_filename = scrapy.Field()
    son_urls = scrapy.Field()
    head = scrapy.Field()
    content = scrapy.Field()


class DoubantvItem(scrapy.Item):
    title = scrapy.Field()
    cover = scrapy.Field()
    url = scrapy.Field()

