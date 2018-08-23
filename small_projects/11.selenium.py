import time
from selenium import webdriver

driver = webdriver.Chrome()

url = 'http://www.baidu.com'


driver.get(url)

# 定位页面input表单
ele_kw = driver.find_element_by_id('kw')
# print(ele_kw)
# 往表单中发送数据
ele_kw.send_keys('python')
# driver.save_screenshot('douban.png')
time.sleep(2)
# driver.close()

# 定位页面搜索按钮
ele_su = driver.find_element_by_id('su')
# 执行点击操作
ele_su.click()

