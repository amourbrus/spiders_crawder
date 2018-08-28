import json
import requests
from lxml import etree
from queue import Queue
import threading


class Qiushi(object):
    def __init__(self):
        self.url = 'https://www.qiushibaike.com/8hr/page/{}'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        self.file = open('qiushi.json', 'w')

        self.urls_queue = Queue()
        self.resp_queue = Queue()
        self.data_queue = Queue()


    def generate_url_list(self):
        self.url_list = [self.url.format(x) for x in range(1, 14)]
        for i in self.url_list:
            self.urls_queue.put(i)
        """方式二：生成一个放一个"""

        # return self.url_list

    def get_data(self):
        while True:
            url = self.urls_queue.get()
            print('正在获取{}对应的响应'.format(url))

            resp = requests.get(url, headers=self.headers)
            self.resp_queue.put(resp.content)
            self.urls_queue.task_done()
            # print(resp.content)
            # return resp.content

    def parse_data(self, ):
        while True:
            data = self.resp_queue.get()
            print('正在解析响应')
            html = etree.HTML(data)
            # 节点　list, 可以是定位的content,也可以是上级???,不可以
            node_list = html.xpath('//*[contains(@id,"qiushi_tag_")]')
            # 段子内容，作者、链接
            # print(node_list)
            data_list = []
            for node in node_list:
                temp = {}
                try:
                    temp['content'] = node.xpath('//*[contains(@id,"qiushi_tag_")]/a[1]/div/span')[0].strip()
                    temp['author'] = node.xpath('//*[contains(@id,"qiushi_tag_")]/div[1]/a[2]/h2/text()')[0]
                    temp['url'] = 'https://www.qiushibaike.com' + node.xpath('//*[contains(@id,"qiushi_tag_")]/a[1]/@href')[0]
                except:
                    temp['content'] = node.xpath('./text()')[0].strip()
                    temp['author'] = "匿名用户"
                    temp['url'] = 'https://www.qiushibaike.com' + node.xpath('//*[contains(@id,"qiushi_tag_")]/a[1]/@href')[0]

                temp['content'] = ''.join([i.strip() for i in node.xpath('./a/div/span/text()')])
                data_list.append(temp)
            self.data_queue.put(data_list)
            self.resp_queue.task_done()
            # return data_list

    def save_data(self, ):
        while True:
            data_list = self.data_queue.get()

            for data in data_list:
                json_data = json.dumps(data, ensure_ascii=False) + ',\n'
                self.file.write(json_data)
            self.data_queue.task_done()

    def __del__(self):
        self.file.close()

    def run(self):
        threading_list = []
        gen_urls_threads = threading.Thread(target=self.generate_url_list)
        threading_list.append(gen_urls_threads)

        # 创建发送请求的线程
        for i in range(3):
            parse_data = threading.Thread(target=self.get_data)
            threading_list.append(parse_data)

        # 创建解析数据的线程
        for x in range(3):
            parse_threads = threading.Thread(target=self.parse_data)
            threading_list.append(parse_threads)

        save_threads = threading.Thread(target=self.save_data)
        threading_list.append(save_threads)

        for t in threading_list:
            t.setDaemon(True)
            t.start()

        for x in [self.urls_queue, self.resp_queue, self.data_queue]:
            x.join()

        # data = self.get_data(self.url)
        # data_list = self.parse_data(data)
        # self.save_data(data_list)


if __name__ == '__main__':
    qiushi = Qiushi()
    qiushi.run()
