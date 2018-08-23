import requests
from lxml import etree


class Gui(object):



    def __init__(self):
        # self.url = 'https://book.km.com/chapter/1344210_1.html'
        # 内容url
        self.content_url = 'https://book.km.com/index.php?c=catch&a=getContent&book_id=1344210&chapter_id={}&sign={}'

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            # 'Referer': 'http://fanyi.youdao.com/',
        }

        self.file = open('gu.txt', 'w')

    def url_list(self):
        # url_list = self.content_url.format([i for i in range])
        for i in range(1, 302):
            url = self.content_url.format(i, )


    def get_data(self, url):
        resp = requests.get(url)
        print(resp.status_code)
        # with open('gui.json', 'wb') as f:
        #     f.write(resp.content)
        return resp.content

    def parse_data(self, data):
        html = etree.HTML(data)
        para_list = html.xpath('//p')
        # print(para_list)
        # data_list = []
        for p in para_list:
            temp = p.xpath('//text()')
            print(temp)
            self.file.write(temp[-1])
            self.file.write('\n')


    def run(self):
        data = self.get_data()
        self.parse_data(data)

if __name__ == '__main__':
    gui = Gui()
    gui.run()

