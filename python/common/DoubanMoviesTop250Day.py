class DoubanMoviesTop250Day:
    def __init__(self):
        # 单个豆瓣数据集的生成时间，格式是"年-月-日"
        self.create_time = ''

        # 按照排名排列的有序的数据
        self.day_data = []
