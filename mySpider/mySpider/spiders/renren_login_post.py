#coding:utf-8

import scrapy

class RenrenSpider(scrapy.Spider):
	name = "renren_login_post"
	allowed_domains = ["renren.com"]
	
	def start_requests(self):
		# 发送post请求
		post_url = "http://www.renren.com/Plogin.do"
		
		formdata = {
			"email": "mr_mao_hacker@163.com",
			"password": "alarmchime"
			}
			
		yield scrapy.FormRequest(post_url, formdata=formdata, callback=self.parse)
		
	def parse(self, response):
		url_list = [
			"http://www.renren.com/410043129/profile",
            "http://www.renren.com/965999739/profile"
        ]
		
		for url in url_list:
			yield scrapy.Request(url, callback=self.parse_page)
			
	def parse_page(self, response):
		file_name = response.xpath("//title/text()").extract_first()
		
		with open(file_name, "w") as f:
			f.write(response.body)
			
	
		