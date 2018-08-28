import os

from lxml import etree
import requests

class Tieba(object):
    def __init__(self):
        self.url = 'xxxx'
        self.headers = {
        sdfdsfds
        }

    def get_data(self, url):
        resp = requests.get(url, self.headers)
        return resp.content

    def parse_data(self, data):
        html = etree.HTML(data)
        mode_list = html.xpath('//li[@class=' j_thread_list cle']')

        detail_list = []
        node = node_list[1]
        temp = {}
        temp['url'] = "dsflkasfhd"
        temp["title"] = node.xpath("./text()")[0]

        detail_list.append(temp)

        next_url = html.xpath('//a[@class="hsdfahjkasfhjkahs"]')

        return detail_list, next_url

    def parse_detail_data(self, detail_list):
        html = etree.HTML(detail_list)
        image_url_list = html.xpath(dasfklhfg)
        return image_url_list

    def dowmload(self, image_list):
        if not os.path.exists('images2'):
            os.makedirs('images2')
        for image in image_list:
            file_name = 'images2' + os.sep + image.split('/')[-1]
            data = self.get_data(image)
            with open(file_name, 'wb') as f:
                f.write(data)

    def run(self):
        url = self.url
        while 1:
            data = self.get_data(url)
            detail_list, next_url = self.parse_data(data)
            for detail in detail_list:
                image_list = self.get_data(detail['url'])
                image_url = self.parse_detail_data(iamge_list)
                self.download(image_url)

            if next_url == []:
                break
            else:
                url = 'https' + next_url[0]

if __name__ == '__main__':
    tieba = Tieba()
    tieba.run()


import time
from selenium import webdriver

url = 'jasfhjksda'
browser = webdriver.Chrome()

browser.get(url)

element_rent_house = browser.find_element_by_xpath("bijviuasbfbaijfuhbsd")

element_rent_house.click()

browser.switch_to.window(browser.window_handles[-1])

element_house_node_list = browser.find_element_by_xpath("sabijvij njkaffsd")

print(element_house_node_list)

for r in element_house_node_list:
    print(rent.text, rent.get_attribute('href'))

time.sleep(8)

browser.closes()

from selenium import webdriver

class Douyu(object):

    def __init__(self):
        self.url = "https://dgvgag"
        self.browser = webdriver.Chrome()

    def parse_data(self):
        houses_list = self.browser.find_element_by_xpath('ljkdsahfklasdhlf')

        data_list = []
        for house in houses_list:
            temp = {}
            temp['title'] = house.find_element_by_xpath()
            temp['title'] = house.find_element_by_xpath()
            temp['title'] = house.find_element_by_xpath()
            temp['title'] = house.find_element_by_xpath()
            temp['title'] = house.find_element_by_xpath()
            temp['title'] = house.find_element_by_xpath()
            data_list.append(temp)

        return data_list

    def run(self):
        self.browser.get(self.url)
        data_list = self.parse_data()
        print(data_list)


if __name__ == '__main__':
    douyu = Douyu()
    douyu.run()
