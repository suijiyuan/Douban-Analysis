# coding:utf-8
from python.analysis import DoubanMoviesTop250Analysis


def main():
    douban_movies_top250_all = DoubanMoviesTop250Analysis.main()

    if douban_movies_top250_all is None:
        print('获取处理后的数据集异常')

    if len(douban_movies_top250_all.all_data) < 2:
        print("数据集中元素个数不满足分析要求，请检查数据集")

    douban_movies_top250_name_set_list = []

    for douban_movies_top250_day_data in douban_movies_top250_all.all_data:
        douban_movies_top250_name_set = set()

        for douban_movies_top250_day_data_item in douban_movies_top250_day_data.day_data:
            douban_movies_top250_name_set.add(douban_movies_top250_day_data_item.movie_name)

        douban_movies_top250_name_set_list.append(douban_movies_top250_name_set)

    dataset_count = 1
    for item in douban_movies_top250_name_set_list:
        print("数据集%d: %s" % (dataset_count, item))
        dataset_count = dataset_count + 1

    # 数据集的个数
    dataset_count = dataset_count - 1

    # 在这里对集合进行运算


if __name__ == '__main__':
    main()
