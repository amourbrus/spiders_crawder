from selenium import webdriver

class Douyu(object):

    def __init__(self):
        self.url = 'https://www.douyu.com/directory/all'
        self.browser = webdriver.Chrome()

    def parse_data(self):
        # 获取房间列表
        houses_list = self.browser.find_elements_by_xpath('//*[@id="live-list-contentbox"]/li')

        data_list = []
        for house in houses_list:
            temp = {}
            temp['title'] = house.find_element_by_xpath('./a')
            temp['type'] = house.find_element_by_xpath('/a/div/div/h3')
            temp['owner'] = house.find_element_by_xpath('/a/div/p/span[1]')
            temp['hot'] = house.find_element_by_xpath('/a/div/p/span[2]')
            temp['cover'] = house.find_element_by_xpath('/a/span/img')

            data_list.append(temp)

        return data_list



    def run(self):
        self.browser.get(self.url)
        # while True:
        data_list = self.parse_data()
        print(data_list)

if __name__ == '__main__':
    douyu = Douyu()
    douyu.run()