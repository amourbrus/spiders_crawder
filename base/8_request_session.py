import requests

url = 'http://www.renren.com/PLogin.do'

headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

post_data = {
    'email': 'ihflzd',
    'password': 'fahhj23435'
}

session = requests.Session()
session.post(url, headers=headers, data=post_data)

# 验证登录是否成功, get请求登录成功后的页面
resp = session.get('http://www.renren.com/438718956/profile')

import re
print(re.findall('风', resp.content.decode()))