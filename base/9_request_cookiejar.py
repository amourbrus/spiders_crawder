import requests

url = 'http://www.baidu.com'
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

response = requests.get(url, headers=headers)
print(response.cookies)
cookiejar = response.cookies
# 动态的获取cookie并转换数据格式‘
cookie_dict = requests.utils.dict_from_cookiejar(cookiejar)
print(cookie_dict)

cookie_jar = requests.utils.cookiejar_from_dict(cookie_dict)
print(cookie_jar)
