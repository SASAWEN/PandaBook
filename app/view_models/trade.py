"""
    Created by cala at 2019-11-01
"""

from app.view_models.book import BookViewModel

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


class MyTrades:
    """
    used for my gifts list and my wishes list
    :param: my_trades_list: the gifts/wishes list of current user
            trade_count_list: the wishes/gifts number of one trade
    """
    def __init__(self, my_trades_list, trade_count_list):
        self.trades = []
        self.__my_trades_list = my_trades_list
        self.__trade_count_list = trade_count_list
        self.trades = self.__parse()

    def __parse(self):
        """

        :return: rst_gifts: a list of dict containing gift id, book view model, wish count
        """
        rst_trades = []
        for gift in self.__my_trades_list:
            # search for wish/gift count of trade by isbn => return isbn, book, book id
            rst_trades.append(self.__matching(gift))

        return rst_trades

    def __matching(self, trade):
        """

        :param gift: Gift()/Wish()
        :return: rst: contains gift/wish id, book view model, wish/gift count
        """
        count = 0
        for item in self.__trade_count_list:
            if item['isbn'] == trade.isbn:
                count = item['count']
                break
        rst = {
            'id': trade.id,
            'book': BookViewModel(trade.book),
            'count': count
        }
        return rst