import re
import requests
import json
# 同２，动态加载


class Guokr(object):
    def __init__(self):
        self.url = 'https://www.guokr.com/ask/highlight/?page=1'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        self.file = open('guokr.json', 'w')

    def get_data(self, url):
        resp = requests.get(url, headers=self.headers)
        # print(resp.content.decode())
        return resp.content.decode()

    def parse_data(self, data):
        # print(title_list)
        #  <a target="_blank" href="(.*?)">(.*?)</a>  使用正则匹配响应的数据,匹配的数据还不是很准确，再加一层<h>
        results = re.findall('<h2><a target="_blank" href="(.*?)">(.*?)</a></h2>', data)
        # print(results)
        data_list = []
        for result in results:
            temp = {}
            temp['url'] = result[0]
            temp['title'] = result[1]
            data_list.append(temp)
        # 解析下一页的链接
        next_url = re.findall('<a href="(/ask/highlight/\?page=\d+)">下一页</a>',data)
        return data_list, next_url
        # print(json_data)

    def save_data(self, data_list):
        for data in data_list:
            json_data = json.dumps(data, ensure_ascii=False) + ',\n'
            self.file.write(json_data)


    def run(self):
        while True:
            data = self.get_data(self.url)
            data_list, next_url = self.parse_data(data)
            self.save_data(data_list)

            self.url = 'https://www.guokr.com' + next_url[0]

            if next_url == []:
                break



if __name__ == '__main__':
    guokr = Guokr()
    guokr.run()