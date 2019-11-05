"""
    Created by cala at 2019-11-05
"""

from app.view_models.book import BookViewModel

class Gifts:
    def __init__(self, my_gifts_list, wish_count_list):
        self.gifts = []
        self.__my_gifts_list = my_gifts_list
        self.__wish_count_list = wish_count_list
        self.gifts = self.__parse()

    def __parse(self):
        """

        :return: rst_gifts: a list of dict containing gift id, book view model, wish count
        """
        rst_gifts = []
        for gift in self.__my_gifts_list:
        # search for wish count of gift by isbn => return isbn, book, book id
            rst_gifts.append(self.__matching(gift))

        return rst_gifts


    def __matching(self, gift):
        """

        :param gift: Gift()
        :return: rst: contains gift id, book view model, wish count
        """
        count = 0
        for item in self.__wish_count_list:
            if item['isbn'] == gift.isbn:
                count = item['count']
                break
        rst = {
            'id': gift.id,
            'book': BookViewModel(gift.book),
            'count': count
        }
        return rst
