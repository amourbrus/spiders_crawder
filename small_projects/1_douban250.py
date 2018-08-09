#coding=utf-8
"""
查看豆瓣页面：
每页有25条电影，共有10页。
每条电影信息都在li标签里

pip install beautifulsoup4
"""
import codecs

import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
}

def download_page(url):
    data = requests.get(url, headers=headers).content
    return data

def parse_html(html):
    soup = BeautifulSoup(html)
    movie_list = soup.find('ol', attrs={'class':'grid_view'})

    movie_name_list = []
    for movie_li in movie_list.find_all('li'):
        detail = movie_li.find('div', attrs={'class':'hd'})
        movie_name = detail.find('span',attrs={'class':'title'}).getText()
        movie_name_list.append(movie_name)

    next_page = soup.find('span', attrs={'class':'next'}).find('a')
    if next_page:
        return movie_name_list, url + next_page['href']
    return movie_name_list,None


def main():
    urls = url
    with codecs.open('movies', 'wb', encoding='utf-8') as f:
        while urls:
            html = download_page(urls)
            movies, urls = parse_html(html)
            f.write(u'{movies}\n'.format(movies='\n'.join(movies)))


if __name__ == '__main__':
    # print(download_page(url))
    main()