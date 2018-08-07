import requests

url = 'https://www.baidu.com/s?'
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

kw = {
    'wd': '天气'
}

# 发送带参数的请求
response = requests.get(url,headers=headers, params=kw)
with open('baidu.html', 'wb') as f:
    f.write(response.content)

# print(response.status_code)
