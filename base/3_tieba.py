import requests

# 完成百度任意贴吧爬虫：任意的页数，保存文件
# 1,构造url
# 2,请求头
# 3,发送请求
# 4,保存文件

class Tieba(object):

    def __init__(self,name,pn):
        self.name = name
        self.url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn='.format(name)
        # 生成url页数列表
        self.url_list = [self.url + str(i*50) for i in range(pn)]
        # 打印页数
        # print(self.url_list)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }

    def get_data(self, url):
        """发送请求，返回数据"""
        response = requests.get(url, headers=self.headers)
        return response

    def save_data(self, data, index):
        file_name = self.name + str(index) + '.html'
        with open(file_name, 'wb') as f:
            f.write(data.content)

    def run(self):
        for url in self.url_list:
            data = self.get_data(url)
            # print(data.status_code, data.url)
            index = self.url_list.index(url)
            self.save_data(data, index)



if __name__ == '__main__':
    tieba = Tieba('世界杯',3)
    tieba.run()
