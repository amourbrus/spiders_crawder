import requests

url = 'https://www.zhihu.com/'

# url = 'http://baidu.com'
# url = 'http://www.sina.com.cn'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

response = requests.get(url, headers=headers)   # 170  93962
# response = requests.request('get', 'url')  # also
# response.url   .encoding  .status_code
print(response.status_code)
print(len(response.content))  # 81,加不加decode都一样
# print(response.content.decode())   # 120006

# print(response.content.decode())
# with open('zhihu.html', 'wb') as f:
#     f.write(response.content)
