from test_wework.page.message.history_msg import HistoryMsg


class TestMsg:

    @classmethod
    def setup(cls):
        cls.msg = HistoryMsg(reuse=True)

    def test_history(self):
        self.msg.history_msg()
