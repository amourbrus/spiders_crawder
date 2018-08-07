import time
from selenium import webdriver

url = 'http://sz.58.com/'

browser = webdriver.Chrome()

browser.get(url)
# 定位租房按钮
ele_rent_house = browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/span[1]/a')

ele_rent_house.click()

#切换到新的窗口
browser.switch_to.window(browser.window_handles[-1])

# 获取租房信息的节点列表
rent_house_node_list = browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[5]/div[2]/ul/li/div[2]/h2/a')

print(rent_house_node_list)

for rent in rent_house_node_list:
    print(rent.text, rent.get_attribute('href'))

time.sleep(8)
browser.close()
# browser.window_handles[-1].close()





