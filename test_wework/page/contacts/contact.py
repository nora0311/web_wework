"""
通讯录 功能界面
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test_wework_selenium.page.base.basepage import BasePage
from test_wework_selenium.page.contacts.add_member import AddMemberPage


class Contact(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def goto_add_member(self):
        add_locator = (By.CSS_SELECTOR, ".js_has_member div:nth-child(1) .js_add_member")
        WebDriverWait(self._driver, 100).until(self.wait_element)
        # self.find(By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member').click()
        return AddMemberPage(reuse=True)

    def wait_element(self, x):
        size = len(self._driver.find_elements(By.ID, 'username'))
        if size < 1:
            self.find(By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member').click()
        return size >= 1

    def goto_import_page(self, filepath):

        pass

    def export_users(self):
        pass

    def set_department(self):
        pass

    def delete(self):
        pass

    def invite(self):
        pass
