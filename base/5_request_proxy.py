import requests

url = 'http://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

# 正向代理：面向对象是客户端，服务器知道客户端是谁！类比使用翻墙工具
# 反向代理：面向对象是服务器,客户端不知道访问的服务器是谁！类比web项目部署使用的Nginx

# 免费代理  类型：HTTP则是只支持http，https都支持
proxy = {
    'http':'http://101.96.9.***:8082',
    # 'https':'http://101.96.9.***:8082'
}

# 付费代理(开发环境下建议使用付费代理)
# proxy = {
#     'http':'http://username:pasword@47.96.239.158:3128',
#     'https':'http://username:pasword@47.96.239.158:3128'
# }


response1 = requests.get(url, headers=headers, proxies=proxy)
print(response1.status_code)
