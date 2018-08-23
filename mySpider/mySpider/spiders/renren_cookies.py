#coding:utf-8

import scrapy

class RenrenSpider(scrapy.Spider):
	name = "renren_cookies"
	allowed_domains = ["renren.com"]
	start_urls = [
		"http://www.renren.com/410043129/profile",
        "http://www.renren.com/965999739/profile"
	]
	
	def start_requests(self):
		cookies = {"anonymid" : "j7wsz80ibwp8x3",
            "_r01_" : "1",
            "ln_uact" : "mr_mao_hacker@163.com",
            "depovince" : "GW",
            "ick_login" : "a50cbea9-3d00-4458-9665-54c6e9557743",
            "first_login_flag" : "1",
            "loginfrom" : "syshome",
            "wp_fold" : "0",
            "JSESSIONID" : "abcXIDq6u5j8b4XKdusuw",
            "_de" : "BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5",
            "id" : "327550029",
            "jebecookies" : "57c3105e-6e27-45b1-a529-38026372c50d|||||",
            "p" : "36a01dc1e912bd6932a15f60174b60be9",
            "ln_hurl" : "http://hdn.xnimg.cn/photos/hdn121/20180807/1115/main_WKP9_0ab200000ea5195a.jpg",
            "t" : "a53991a23060e9ec4810b9515d82d1509",
            "societyguester" : "a53991a23060e9ec4810b9515d82d1509",
            "xnsid" : "ed9988de"
		
		}
		
		headers = {
            "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding" : "gzip, deflate",
            "Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control" : "max-age=0",
            "Connection" : "keep-alive",
            "Host" : "www.renren.com",
            "Upgrade-Insecure-Requests" : "1",
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }
		
		for url in self.start_urls:
			yield scrapy.Request(url, cookies=cookies, headers=headers, callback=self.parse_page
			)
			
	def parse_page(self, response):
		file_name = response.xpath("//title/text()").extract_first()
		with open(file_name, 'w') as f:
			f.write(response.body)
			
		
		
		
		
		
		