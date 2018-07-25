import requests
import json

"""
金山在线翻译
post请求
url/请求头
发送请求，获取响应
"""
class King(object):

    def __init__(self, kw):
        self.url = 'http://fy.iciba.com/ajax.php?a=fy'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        self.data={
            'f': 'auto',
            't': 'auto',
            'w': kw,
        }

    def get_data(self):
        resp = requests.post(url=self.url, headers=self.headers, data=self.data)
        print(resp.content.decode())  # bytes   b'{}'
        return resp.content.decode()  # str   { }

    def parse_data(self, data):
        result = json.loads(data)
        try:
            # 中文翻译, 查看浏览器　response
            print(result['content']['out'])
        except:
            print(result['content']['word_mean'])

    def run(self):
        data = self.get_data()
        self.parse_data(data)

import sys

if __name__ == '__main__':
    kw = sys.argv[1]   # 运行时控制台的输入，0为该文件
    print(kw)
    king = King(kw)
    king.run()
