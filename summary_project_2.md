# 1,爬取豆瓣电影top250
*使用requests, bs4
采用下一页的方式获取全部数据*


# 2,豆瓣tv--美剧为例
*使用requests, response数据格式为json
采用偏置获取下一页,json数据存储*

```python
self.offset += 20
if not data_list:
    break
```

# 3, 果壳网问答爬取标题
*使用requests, response是 html页面，数据也在
分析页面，点击精彩问答，很容易找到 url  https://www.guokr.com/ask/highlight/
再经过 点击下一页  https://www.guokr.com/ask/highlight/?page=2
使用正则匹配下一页
使用正则匹配数据：
<a target="_blank" href="https://www.guokr.com/question/652960/">陆游这句诗“人生若要常无事，两颗梨需手自煨。”是什么意思？是养生方法吗？</a>
<a target="_blank" href="(.*?)">(.*?)</a> 使用正则匹配响应的数据,匹配的数据还不是很准确，再加一层<h>*

# 4, 36kr新闻信息
使用requests, 动态加载页面response是json,使用正则解析页面，判断循环结束以是否拿到ajax_data为准

有一个坑，拿不到数据， ---- 针对第一页而言，可以不用这种方式，直接用后面的ajax加载。
        # 要学会将响应写入文件来查看哪些格式错误，才有下步的spilt
        # with open('temp.json', 'w') as f:
        #     f.write(results)
        json_data = results.split(',locationnal={')[0]


# 5, 有道翻译

使用post 提交，　构建表单数据是重点
headers中用到了　cookie 　　referer
构建数据　－－　分析Ｊｓ
时间戳的处理
md5的加密
```python
md5=hashlib.md5()
md5.update(str_data.encode())
md5.hexdigest()
```

# 6, 贴吧图片下载
使用requests模块
数据response   HTML, 使用xpath解析页面－－页面分析
1、如果使用浏览器和network的response中都能够看到数据，但是，在代码中拿不到，可以把响应数据写入本地文件；
2、百度贴吧的响应数据是放入注释中的，使用xpath获取不到，可以使用正则；
3、可以尝试修改请求信息；使用比较古老的user-agent；
url提取需要拼接，存图片

# 7, 糗事百科
翻页
requests, 使用xpath解析页面，注意 *匿名用户*

# 8,多线程糗事百科爬取
```python
from queue import Queue
import threading

queue_obj.put()
queue_obj.get()
使用线程池，在发送请求和解析响应分开，以守护线程方式启动
for t in threading_list:
        t.setDaemon(True)
        t.start()

    for x in [self.urls_queue, self.resp_queue, self.data_queue]:
        x.join()

```
# 9, selenium　基本使用
先要安装驱动
```python
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


```

# 10, 58同城抓取
selenium  

```python
1,创建浏览器对象
2,browser_obj.find_element_by_xpath("vbjabd")
3,click or 上述是node_list,遍历再xpath() get what you want

```


# 11,douyu  获取所有房间信息
selenium
find_element_by_xpath, get_attribute
