"""
管理工具简单测试
"""
from test_wework.page.manage_tools.managetools import ManageTools


class TestManageTools:

    def setup(self):
        self.manage = ManageTools(reuse=True)

    # 上传素材
    def test_pic_material(self):
        self.manage.material().pic_material(
            "/Users/serenehoo/PycharmProjects/Selenium_pro/test_contact_selenium/testcase/rose.jpg")

    # 消息群发
    def test_send_message(self):
        message = self.manage.send_message()
        message.send_group_message(app="两只猫猫", content="content", group="腾讯公司")
