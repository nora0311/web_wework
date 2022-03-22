"""
素材库 testcase

"""
import pytest

from test_wework.page.manage_tools.managetools import ManageTools
from test_wework.page.manage_tools.material import Material


class TestMaterial():

    @classmethod
    def setup(cls):
        cls.manage = ManageTools(reuse=True)
        cls.material = Material(reuse=True)

    #  管理工具-素材库入口
    def test_pic_material(self):
        self.manage.goto_material().pic_material(
            "/Users/serenehoo/Desktop/PythonProj/web_wework/test_wework/testcase/rose.jpg")

    @pytest.mark.parametrize("content",["文字测试","文字测试 1"])
    def test_text_material(self,content):
        # self.material.text_material()
        self.manage.goto_material().text_material(content)
