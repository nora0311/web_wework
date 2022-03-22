from selenium.webdriver.common.by import By

from test_wework.page.base.basepage import BasePage
from test_wework.page.login.registry import Registry


class Login(BasePage):

    # https://work.weixin.qq.com/

    def goto_register(self):
        # self._driver.find_element(By.CSS_SELECTOR,'.login_registerBar_link').click()
        self._driver.find_element(By.LINK_TEXT, '企业注册').click()
        return Registry(reuse=True)

    def login_success(self):
        pass

    def login_fail(self):
        pass

