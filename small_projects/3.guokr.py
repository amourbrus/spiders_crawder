import requests
import json
# 同２，动态加载

from bs4 import BeautifulSoup


class Guokr(object):
    def __init__(self):
        self.url = 'https://www.guokr.com/scientific/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }

    def get_data(self, url):
        resp = requests.get(url, headers=self.headers)
        # print(resp.content.decode())
        return resp.content.decode()

    def parse_data(self, data):
        soup = BeautifulSoup(data)
        title_list =  soup.find('div', attrs={'class':'article-list'})
        # print(title_list)
        movie_name_list = []
        for article_li in title_list.find_all('div'):
            article_name = article_li.find('a', attrs={'class': 'article-title'})
            movie_name_list.append(article_name)
        print(movie_name_list)

    def run(self):
        data = self.get_data(self.url)
        self.parse_data(data)
if __name__ == '__main__':
    guokr = Guokr()
    guokr.run()