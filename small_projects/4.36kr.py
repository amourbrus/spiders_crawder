"""动态加载，新闻信息，正则"""
import json
import re
import requests


class Kr36(object):

    def __init__(self):
        self.url = 'http://36kr.com/'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        self.file = open('36kr.json', 'w')
# http://36kr.com/api/search-column/mainsite?per_page=20&page=2&_=1532767531372
        self.ajax_url = 'http://36kr.com/api/search-column/mainsite?per_page=20&page={}'
        self.page = 2


    def get_data(self, url):
        resp = requests.get(url, headers=self.headers)
        # print(resp.content)
        return resp.content.decode()

    def parse_data(self, data):
        # <script>var props=(.*?)</script>
        results = re.findall('<script>var props=(.*?)</script>', data)[0]
        # print(results)
        # 要学会将响应写入文件来查看哪些格式错误，才有下步的spilt
        # with open('temp.json', 'w') as f:
        #     f.write(results)
        json_data = results.split(',locationnal={')[0]
        # print(json_data)
        dict_data = json.loads(json_data)
        # 获取响应中的新闻列表
        news_list = dict_data["hotPosts|hotPost"]
        data_list =[]
        for news in news_list:
            temp = {}
            temp['title'] = news['title']
            temp['summary'] = news['summary']
            temp['cover'] = news['cover']
            data_list.append(temp)

        # print(data_list)
        return data_list

    def parse_ajax_data(self, data):
        dict_data = json.loads(data)
        news_list = dict_data['data']['items']
        data_list =[]
        for news in news_list:
            temp = {}
            temp['title'] = news['title']
            temp['summary'] = news['summary']
            temp['cover'] = news['cover']
            data_list.append(temp)
        return data_list

    def save_data(self, data_list):
        for data in data_list:
            json_data = json.dumps(data, ensure_ascii=False,) + ',\n'
            self.file.write(json_data)

    def __del__(self):
        self.file.close()


    def run(self):
        data = self.get_data(self.url)
        data_list = self.parse_data(data)
        self.save_data(data_list)
        # 加载下一页数据，开启循环， --可以合并
        while True:
            url = self.ajax_url.format(self.page)
            data = self.get_data(url)
            ajax_data = self.parse_ajax_data(data)
            self.save_data(ajax_data)
            if ajax_data == []:
                break
            self.page += 1


if __name__ == '__main__':
    kr36 = Kr36()
    kr36.run()
