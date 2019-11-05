"""
    Created by cala at 2019-11-01
"""


class TradeInfo():
    """
    This model is to show the list of users who want the book and who send the book.
    :param goods: book(wish, gift) list
    """
    def __init__(self, goods):
        self.total = 0
        self.trades = []

    def __parse(self, goods):
        self.total = len(goods)

    def __map_to_trade(self, single_good):
        if single_good.create_datetime:
            # strftime: 格式化操作 转化成string类型
            time = single_good.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'
        return dict(
            user_name = single_good.user.nickname,
            time = time,
            id = single_good.id
        )

