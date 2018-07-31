import json
import requests
from lxml import etree


class Qiushi(object):
    def __init__(self):
        self.url = 'https://www.qiushibaike.com/8hr/page/{}'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        self.file = open('qiushi.json', 'w')

    def generate_url_list(self):
        self.url_list = [self.url.format(x) for x in range(1, 14)]
        return self.url_list

    def get_data(self, url):
        resp = requests.get(url, headers=self.headers)
        # print(resp.content)
        return resp.content

    def parse_data(self, data):
        html = etree.HTML(data)
        # 节点　list, 可以是定位的content,也可以是上级???
        node_list = html.xpath('//*[contains(@id,"qiushi_tag_")]/a[1]/div/span[1]')
        # 段子内容，作者、链接
        print(node_list)
        data_list = []
        for node in node_list:
            temp = {}
            try:
                temp['content'] = node.xpath('//*[contains(@id,"qiushi_tag_")]/a[1]/div/span')[0].strip()
                temp['author'] = node.xpath('//*[contains(@id,"qiushi_tag_")]/div[1]/a[2]/h2/text()')[0]
                temp['url'] = 'https://www.qiushibaike.com' + node.xpath('//*[contains(@id,"qiushi_tag_")]/a[1]/@href')[
                    0]
            except:
                temp['content'] = node.xpath('./text()')[0].strip()
                temp['author'] = "匿名用户"
                temp['url'] = 'https://www.qiushibaike.com' + node.xpath('//*[contains(@id,"qiushi_tag_")]/a[1]/@href')[
                    0]

            data_list.append(temp)

        return data_list

    def save_data(self, data_list):
        for data in data_list:
            json_data = json.dumps(data, ensure_ascii=False) + ',\n'
            self.file.write(json_data)

    def __del__(self):
        self.file.close()

    def run(self):
        data = self.get_data(self.url)
        data_list = self.parse_data(data)
        self.save_data(data_list)


if __name__ == '__main__':
    qiushi = Qiushi()
    qiushi.run()
