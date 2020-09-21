# coding:utf-8

import os

from python.common.DoubanMoviesTop250All import DoubanMoviesTop250All
from python.common.DoubanMoviesTop250Day import DoubanMoviesTop250Day
from python.common.DoubanMoviesTop250Item import DoubanMoviesTop250Item


def main():
    douban_movies_top250_file_prefix = 'douban_movies_top250'
    datasets_directory_path = '../../datasets'

    datasets_directory_file_name_list = os.listdir(datasets_directory_path)

    if datasets_directory_file_name_list is None:
        print("数据集名称列表获取异常, 地址: %s" % datasets_directory_path)
        return

    douban_movies_top250_file_list = [val for val in datasets_directory_file_name_list if
                                      val.startswith(douban_movies_top250_file_prefix)]

    douban_movies_top250_all = DoubanMoviesTop250All()

    for douban_movies_top250_file_name in douban_movies_top250_file_list:
        file_name = datasets_directory_path + '/' + douban_movies_top250_file_name
        with open(file_name, 'r') as douban_movies_top250_file:
            douban_movies_top250_day = DoubanMoviesTop250Day()
            create_time = file_name[len(douban_movies_top250_file_prefix) + 1:]
            douban_movies_top250_day.create_time = create_time

            douban_movies_top250_file_lines = douban_movies_top250_file.readlines()
            rank_count = 1
            for douban_movies_top250_file_line in douban_movies_top250_file_lines:
                douban_movies_top250_item_elements = douban_movies_top250_file_line.split(',')
                if len(douban_movies_top250_item_elements) < 8:
                    print("解析单行记录异常, 单行记录: %s" % douban_movies_top250_file_line)
                    return

                douban_movies_top250_item = DoubanMoviesTop250Item()
                douban_movies_top250_item.rank = rank_count
                rank_count = rank_count + 1
                douban_movies_top250_item.fraction = float(douban_movies_top250_item_elements[0])
                douban_movies_top250_item.movie_name = douban_movies_top250_item_elements[1]
                douban_movies_top250_item.year = douban_movies_top250_item_elements[2]
                douban_movies_top250_item.country = douban_movies_top250_item_elements[3]
                douban_movies_top250_item.type = douban_movies_top250_item_elements[4]

                douban_movies_top250_day.day_data.append(douban_movies_top250_item)

            douban_movies_top250_all.all_data.append(douban_movies_top250_day)

    return douban_movies_top250_all


if __name__ == '__main__':
    main()
