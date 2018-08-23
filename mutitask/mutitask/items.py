# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MutitaskItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TencentItem(scrapy.Item):
    name = scrapy.Field()
    detailLink = scrapy.Field()
    positionInfo = scrapy.Field()
    peopleNumber = scrapy.Field()
    workLocation = scrapy.Field()
    publishTime = scrapy.Field()

class DongguanItem(scrapy.Item):
    """东莞阳光热线"""
    # 每个帖子的titel
    title = scrapy.Field()
    # 每个帖子的编号
    number = scrapy.Field()
    # 每个帖子的文字
    # content = scrapy.field()
    # 每个帖子的url
    url = scrapy.Field()


class DoubanCommentItem(scrapy.Item):
    """豆瓣影评"""
    text = scrapy.Field()

