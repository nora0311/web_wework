"""
添加服务帐号界面
"""
from time import sleep

from selenium.webdriver.common.by import By

from test_wework.page.base.basepage import BasePage


class StaffService(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#/kefu/interior"

    def add_service_account(self):
        self.find(By.LINK_TEXT, '添加服务帐号').click()
        sleep(3)
        # 员工帐号添加界面
        pass
