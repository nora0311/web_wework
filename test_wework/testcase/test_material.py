"""
素材库 testcase

"""
from test_wework.page.manage_tools.managetools import ManageTools
from test_wework.page.manage_tools.material import Material


class TestMaterial():

    @classmethod
    def setup(cls):
        cls.manage = ManageTools(reuse=True)
        cls.material = Material(reuse=True)

    #  管理工具-素材库入口
    def test_pic_material(self):
        self.manage.material().pic_material(
            "/Users/serenehoo/PycharmProjects/Selenium_pro/test_contact_selenium/testcase/rose.jpg")

    def test_text_material(self):
        # self.material.text_material()
        self.manage.material().text_material("试下弹出")
