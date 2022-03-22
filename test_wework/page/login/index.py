"""
url:https://work.weixin.qq.com/
未登录的 main 页面
立即注册-注册界面

"""
from selenium.webdriver.common.by import By

from test_wework.page.base.basepage import BasePage
from test_wework.page.login.login import Login
from test_wework.page.login.registry import Registry


class Index(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    # 去注册
    def goto_register(self):
        self.find(By.LINK_TEXT, '立即注册').click()
        # self.find(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').clck()
        return Registry(reuse=True)

    # 去登录
    def goto_login(self):
        # self._driver = webdriver.Chrome()
        self.find(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return Login(reuse=True)
