### 页面分析

首页文字关于系统　－－－　历史数据查询，所有城市--》每月--》每天的数据
1. 获取每个城市的链接（静态）：
    https://www.aqistudy.cn/historydata/  -
    "//div[@class='all']//a/@href"

    全部城市　按字母分类排序　每个ｕｌ标签一个字母　ul/div[2]/li/a  到城市名　--xpath开始索引为１，这是方式一，方式二，对于有相同重复的如热门城市和全部城市，那就找上级，不同为止，多使用//相对位置

2. 获取每个城市所有月的链接（动态）：
    "//tbody/tr/td/a/@href"

3. 获取每个月的所有天的数据（动态）：
    tr_list = "//tbody/tr"
    tr_list.pop(0)

    for tr in tr_list:
        tr.xpath("./td[1]/text()")
        tr.xpath("./td[2]/text()")
        tr.xpath("./td[3]/span/text()")
        tr.xpath("./td[4]/text()")
        tr.xpath("./td[5]/text()")
        tr.xpath("./td[6]/text()")
        tr.xpath("./td[7]/text()")
        tr.xpath("./td[8]/text()")
        tr.xpath("./td[9]/text()")

### 编码
items.py
spiders.py
  - 获取页面其他数据－－上级中的城市名
    - 方法一：使用meta参数传递
    - 方法二：url中有
      - ｕｒｌ处理方法：
      ```python
      # 或者使用　第三方　six
      # response.url = "https://www.aqistudy.cn/historydata/daydata.php?city=%E6%B7%B1%E5%9C%B3&month=2014-02"

       import six
       if six.PY2:
           "表示python2的环境"
           import urllib
       elif six.PY3:
           "表示python3的环境"
        # =======================================
        try:
            import urllib.parse as urllib
        except ImportError:
            import urllib

        # urllib.parse.unquote()
        url = response.url
        urlencode_str = url[url.find("=")+1:url.find("&")]
        utf8_str = urllib.unquote(urlencode_str)
        city = utf8_str.decode("utf-8")

      ```
middlewares.py **掌握**
* 静态页面交给下载器，动态使用中间件拦截并返回
* 中间件使用selenim浏览器渲染（无界面方式）
* retry的使用   

crawl spider
添加规则 rules
只需要 parse_days函数

RedisSpider



city = 城市
date = 日期
aqi = AQI
level = 质量等级
pm2_5 = PM2.5
pm10 = PM10
so2 = SO2
co = CO
no2 = NO2
o3 = O3_8h
time = datetime.now()
spider = spider.name
