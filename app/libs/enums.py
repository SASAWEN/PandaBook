"""
    Created by cala at 2019-11-17
"""

from enum import Enum

class PendingStatus(Enum):
    Waiting = 1
    Success = 2
    Reject = 3
    Redraw = 4

    @classmethod
    def pending_str(cls, status, role):
        """

        :param status: Pending status
        :param role: current_user role: sender or receiver
        :return: trading status message
        """
        key_map = {
            1: {
                'sender': '等待邮寄',
                'receiver': '等待对方邮寄'
            },
            2: {
                'sender': '书籍已发出，交易完成',
                'receiver': '对方已邮寄，等待收货'
            },
            3: {
                'sender': '您已拒绝赠送',
                'receiver': '对方拒绝赠送'
            },
            4: {
                'sender': '对方已撤销索要',
                'receiver': '您已撤销索要'
            }
        }

        return key_map[status][role]