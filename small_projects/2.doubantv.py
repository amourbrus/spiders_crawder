# coding=utf-8
import requests
import json

class Douban(object):

    def __init__(self):
        self.url =  'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=20&page_start={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        self.file = open('douban.json', 'w')
        self.offset = 0

    def get_data(self, url):
        resp = requests.get(url, headers=self.headers)
        # print(resp.content.decode())
        return resp.content.decode()

    def parse_data(self, data):
        dict_data = json.loads(data)
        results = dict_data['subjects']
        data_list = []
        for tv in results:
            temp = {}
            temp['title'] = tv['title']
            temp['cover'] = tv['cover']
            temp['url'] = tv['url']
            data_list.append(temp)
        return data_list

    def save_data(self, data_list):
        for data in data_list:
            json_data = json.dumps(data, ensure_ascii=False) + ',\n'
            self.file.write(json_data)

    def run(self):
        while True:
            # url = self.url
            # 构造url，动态的加载下一页
            url = self.url.format(self.offset)
            data = self.get_data(url)
            data_list = self.parse_data(data)
            # print(data_list)
            self.save_data(data_list)

            self.offset += 20
            if not data_list:
                break


    def __del__(self):
        self.file.close()


if __name__ == '__main__':
    douban = Douban()
    douban.run()