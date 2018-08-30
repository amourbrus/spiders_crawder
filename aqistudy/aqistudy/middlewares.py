# coding: utf-8
import time

from retrying import retry
from selenium import webdriver

from scrapy.http import HtmlResponse

class AqiSeleniumMiddleware(object):

    def __init__(self):
        # self.driver = webdriver.Chrome()
        # #使用无界面的方式
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(ChromeOptions=self.options)



    # retry会捕获retry_load_page()的异常
    # 如果出现异常则表示数据没有找到，则每次间隔200毫秒，总共尝试20次
    # 如果20次内，数据找到了，则正常向下执行
    @retry(stop_max_attempt_number=20, wait_fixed=200)
    def retry_load_page(self, request, spider):
        try:
            self.driver.find_element_by_xpath("//div[@class='row']//tbody/tr/td[1]")
        except:
            spider.logger.info("Retry {} page ({} times)".format(request.url,self.count ))
            self.count += 1
            raise Exception("<{}> page load failed.".format(request.url))

    def process_request(self, request, spider):
        # 判断是否是动态页面　－－ url 有无php,或者参数monthdata
        if "monthdata" in request.url or "daydate" in request.url:
            self.count = 1
            self.driver.get(request.url)

            try:
                self.retry_load_page(request, spider)
                html = self.driver.page_source  # page_source属性
                return HtmlResponse(
                    url = self.driver.current_url,　　# current_url 属性
                    body = html.encode("utf-8"),
                    encoding = 'utf-8',
                    request = request,
                )
            except Exception as e:
                spider.logger.error(e)


    def __del__(self):
        self.driver.quit()
