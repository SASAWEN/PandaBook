"""
    Created by cala at 2019-11-17
"""

from app.libs.enums import PendingStatus

class TradingCollection:
    """
    Two kinds of view form: sender or receiver
    sender: status "等待邮寄"
    receiver: status "等待收货"
    """
    def __init__(self, tradings, current_user_id):
        self.data = []
        self.data = self.__parse(tradings, current_user_id)

    def __parse(self, tradings, current_user_id):
        return [TradingViewModel(trading, current_user_id).data for trading in tradings]


class TradingViewModel:
    def __init__(self, trade, current_user_id):
        self.data = {}

        self.data = self.__parse(trade, current_user_id)

    @staticmethod
    def sender_or_receiver(trade, current_user_id):
        if trade.receiver_id == current_user_id:
            youare = 'receiver'
        else:
            youare = 'sender'
        return youare

    def __parse(self, trade, current_user_id):
        you_are = self.sender_or_receiver(trade, current_user_id)
        pending_status = PendingStatus.pending_str(trade.pending, you_are)
        r = {
            'you_are': you_are,
            'trade_id': trade.id,
            'status': trade.pending,
            'book_title': trade.book_title,
            'book_author': trade.book_author,
            'book_img': trade.book_img,
            'date': trade.create_datetime.strftime('%Y-%m-%d'),
            'operator': trade.sender_nickname if you_are == 'sender' else trade.recipient_name,
            'recipient_name': trade.recipient_name,
            'address': trade.address,
            'mobile': trade.mobile,
            'message': trade.message,
            'status_str': pending_status
        }
        return r