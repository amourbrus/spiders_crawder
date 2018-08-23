# coding=utf8
import json

from lxml import etree

import requests


class Douban(object):

    def __init__(self):
        self.url = 'https://movie.douban.com/subject/26985127/comments?start={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        self.file = open('doubanc.json', 'w')

    def gen_urls(self):
        self.url_list = [self.url.format(x) for x in range(0,201,20)]
        return self.url_list

    def get_data(self, url):
        resp = requests.get(url, headers=self.headers)
        # print(resp.content)
        return resp.content

    def parse_data(self, data):
        html = etree.HTML(data)
        node_list = html.xpath('//*[@class="comment-item"]//p/span')
        texts = []
        for node in node_list:
            temp = {}
            temp['comments'] = node.xpath('//p/span/text()')
            texts.append(temp)
            yield texts
        # next_url = append
        # print(texts)
        # return texts

    def save_data(self, text):
        for data in text:
            json_data = json.dumps(data, ensure_ascii=False) + ',\n'

            self.file.write(json_data.encode('utf-8'))  # encode要搞清楚


    def run(self):

        for url in self.gen_urls():
            data = self.get_data(url)
            texts = self.parse_data(data)
            self.save_data(texts)


if __name__ == '__main__':
    douban = Douban()
    douban.run()