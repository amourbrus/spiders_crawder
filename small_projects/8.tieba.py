import os

from lxml import etree

import requests


class Tieba(object):

    def __init__(self):
        """
        1、如果使用浏览器和network的response中都能够看到数据，但是，在代码中拿不到，可以把响应数据写入本地文件；
        2、百度贴吧的响应数据是放入注释中的，使用xpath获取不到，可以使用正则；
        3、可以尝试修改请求信息；使用比较古老的user-agent；
        """
        self.url = 'http://tieba.baidu.com/f?ie=utf-8&kw={}'.format('头像')
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }



    def get_data(self, url):
        resp = requests.get(url, self.headers)

        # print(resp.content.decode())
        return resp.content  # todo 什么时候需要解码

    def parse_data(self, data):
        html = etree.HTML(data)
        node_list = html.xpath('//li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a')    # 解析后类型是list，todo　是按楼层顺序的吗？
        # todo 为什么class后面要　空格才有用
        # with open('temp.html', 'w') as f:
        #     f.write(data)
        # print(type(node_list))

        detail_list = []
        # for node in node_list:
        node = node_list[1]   # 选择测试其中一层楼
            # 遍历节点列表,获取列表页面贴吧的title和贴吧详情页面的url
            # 第一页第几层楼
            # 打开for 后下面三行缩进
        temp = {}
        temp['url'] = 'http://tieba.baidu.com' + node.xpath('./@href')[0]   # todo　为什么要０
        temp['title'] = node.xpath('./text()')[0]


        detail_list.append(temp)
        next_url = html.xpath('//a[@class="next pagination-item"]/@href')

        return detail_list, next_url

    def parse_detail_data(self, detail_list):
        html = etree.HTML(detail_list)
        # next_url_list = html.xpath('//*[@id="thread_theme_7"]/div[1]/ul/li[1]/a/@href')   # 改进的，详情页下一页


        image_url_list = html.xpath('//*[contains(@id,"post_content_")]/img/@src')


        return image_url_list

    # 下载图片,创建文件夹，用来保存图片，　　图片存储的顺序，是按顺序来的
    def download(self, image_list):
        if not os.path.exists('images2'):
            os.makedirs('images2')
        for image in image_list:
            print(image, type(image))

            file_name = 'images2' + os.sep + image.split('/')[-1]
            data = self.get_data(image)
            with open(file_name, 'wb') as f:
                f.write(data)


    def run(self):
        url = self.url
        while True:
            data = self.get_data(url)
            detail_list, next_url = self.parse_data(data)
            for detail in detail_list:
                image_list = self.get_data(detail['url'])
                image_url = self.parse_detail_data(image_list)
                self.download(image_url)

            if next_url == []:
                break
            else:
                url = 'https' + next_url[0]

if __name__ == '__main__':
    tieba = Tieba()
    tieba.run()