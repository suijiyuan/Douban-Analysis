# coding:utf-8

import requests
from lxml import html
import re
import time


# 获取豆瓣电影top250的数据
def main():
    url_template = 'https://movie.Douban.com/top250?start=%d'
    index_start = 0
    index_step = 25
    index_max = 250

    year_pattern = re.compile(r'\d{4}')

    file_name = '../../datasets/douban_movies_top250_' + time.strftime("%y_%m_%d", time.localtime()) + '.csv'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/85.0.4183.102 Safari/537.36 '
    }

    with open(file_name, 'w') as file:
        for index in range(index_start, index_max, index_step):
            url = url_template % index
            content = requests.get(url, headers=headers).content
            tree = html.fromstring(content)

            for i in tree.xpath('//div[@class="info"]'):
                if i.xpath('div[@class="hd"]/a/span[@class="title"]/text()'):
                    title = i.xpath('div[@class="hd"]/a/span[@class="title"]/text()')[0]
                else:
                    title = None
                info = i.xpath('div[@class="bd"]/p[1]/text()')
                if len(info) == 2:
                    # 注意下面的空格是不同的，有特殊字符
                    actors = info[0].replace(' ', '').replace('\n', '').replace('主演:', '').replace('导演:', '') \
                        .replace('   ', ' ')
                    if len(info[1].replace(' ', '').replace(' ', '').replace('\n', '').split('/')) >= 3:
                        date = ''
                        for date_index in range(
                                len(info[1].replace(' ', '').replace(' ', '').replace('\n', '').split('/')) - 2):
                            year_data = info[1].replace(' ', '').replace(' ', '').replace('\n', '').split('/')[
                                date_index]
                            year_match = year_pattern.search(year_data)
                            if year_match:
                                date += year_match.group() + '/'
                        date = date[:-1]
                        country = info[1].replace(' ', '').replace(' ', '').replace('\n', '').split('/')[-2]
                        movie_type = info[1].replace(' ', '').replace(' ', '').replace('\n', '').split('/')[-1]
                    else:
                        date = None
                        country = None
                        movie_type = None
                else:
                    actors = None
                    date = None
                    country = None
                    movie_type = None
                if i.xpath('div[@class="bd"]/div[@class="star"]/span[2]/text()'):
                    rate = i.xpath('div[@class="bd"]/div[@class="star"]/span[2]/text()')[0]
                else:
                    rate = None
                if i.xpath('div[@class="bd"]/div[@class="star"]/span[4]/text()'):
                    comment_count = i.xpath('div[@class="bd"]/div[@class="star"]/span[4]/text()')[0].replace('人评价', '')
                else:
                    comment_count = None
                if i.xpath('div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()'):
                    quote = i.xpath('div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()')[0]
                else:
                    quote = None
                print(rate, title, date, country, movie_type, actors, quote, comment_count)
                file.write('%s,%s,%s,%s,%s,%s,%s,%s\n' % (
                    rate, title, date, country, movie_type, actors, quote, comment_count))


if __name__ == '__main__':
    main()
