# coding utf-8
import scrapy

from ..items import AqistudyItem

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

from scrapy_redis.spiders import RedisCrawlSpider


class AqiSpider(RedisCrawlSpider):
    # 爬虫名
    name = "aqi_rediscrawlspider"
    # 允许爬虫抓取的域名
    allowed_domains = ['aqistudy.cn']
    # 入口url
    base_url = "https://www.aqistudy.cn/historydata/"
    # start_urls = [base_url]
    redis_key = "aqirediscrawlspider:start_urls"

    rules = [
        # 获取每个城市（384城市）的链接，并发送请求，返回的响应继续提取链接（但是在第一个Rule中已经无法提取新的链接，但是在第二个Rule中可以提取每个城市所有月的链接）
        Rule(LinkExtractor(allow=r"monthdata"), follow=True),
        # 获取每个城市所有月的链接，并发送请求返回响应，交给callback解析该月所有天的数据，同时不再需要继续提取链接。
        Rule(LinkExtractor(allow=r"daydata"),callback="parse_day", follow=False)
    ]

    # def parse(self, response):
    #     """
    #         解析start_urls的响应，　解析提取每个城市的城市链接和城市名
    #     """
    #     city_link_list = response.xpath("//div[@class='all']//a/@href").extract()
    #     city_name_list = response.xpath("//div[@class='all']//a/text()").extract()
    #
    #     for city_link, city_name in zip(city_link_list, city_name_list)[20:23]:
    #         yield scrapy.Request(self.base_url + city_link, meta={"city":city_name}, callback=self.parse_month)
    #
    # def parse_month(self, response):
    #     # 解析每个城市的响应，提取每个月的链接并发送请求，注意请求主页面的不是右侧的索引块－－数据不全
    #     month_link_list = response.xpath("//tbody/tr//td//a/@href").extract()
    #     for month_link in month_link_list[10:13]:  # 取少量做测试
    #         yield scrapy.Request(self.base_url + month_link, meta=response.meta,callback=self.parse_day)


    def parse_day(self, response):
        # 解析每个月的响应，提取所有天的数据并保存在item中
        tr_list = response.xpath("//tbody/tr")
        tr_list.pop(0)  # delete th
        city = response.meta['city']

        for tr in tr_list:
            item = AqistudyItem()
            item['city'] = city
            item['date'] = tr.xpath('./td[1]/text()').extract_first()
            item['aqi'] = tr.xpath('./td[2]/text()').extract_first()
            item['level '] = tr.xpath('./td[3]/span/text()').extract_first()
            item['pm2_5 '] = tr.xpath('./td[4]/text()').extract_first()
            item['pm10 '] = tr.xpath('./td[5]/text()').extract_first()
            item['so2 '] = tr.xpath('./td[6]/text()').extract_first()
            item['co '] = tr.xpath('./td[7]/text()').extract_first()
            item['no2 '] = tr.xpath('./td[8]/text()').extract_first()
            item['o3 '] = tr.xpath('./td[9]/text()').extract_first()

            yield item
