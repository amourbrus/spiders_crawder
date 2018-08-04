import requests
import time
from selenium import webdriver


class Guichuideng(object):
    def __init__(self):
        self.url = 'https://book.km.com/chapter/1344210_1.html'
        self.browser = webdriver.Chrome()
        self.file = open('gui.txt','w')
    # def get_data(self):
    #     resp = requests.get(self.url)
    #     print(resp.status_code)
    #     with open('book.html', 'wb') as f:
    #         f.write(resp.content)


    # 每一页的内容
    def parse_data(self):
        para_list = self.browser.find_elements_by_xpath('//*[@id="xtopjsinfo"]/div[2]/div[2]/div/div[2]/p')
        title = self.browser.find_element_by_xpath('//*[@id="xtopjsinfo"]/div[2]/div[2]/div/div[1]/h1').text
        self.file.write(title)
        self.file.write('\n')
        for i in para_list:
            text = i.text

            self.file.write('\t\t')
            self.file.write(text)
            self.file.write('\n')

            # print(text)


    def run(self):
        self.browser.get(self.url)
        self.parse_data()
        while True:
            try:
                next_page_url = self.browser.find_element_by_xpath('//*[@id="xtopjsinfo"]/div[2]/div[2]/div/div[4]/a[2]')
                next_page_url.click()
                self.parse_data()
                time.sleep(5)
            except:
                self.parse_data()
            finally:
                if not next_page_url:
                    break


if __name__ == '__main__':
    gui = Guichuideng()
    gui.run()
