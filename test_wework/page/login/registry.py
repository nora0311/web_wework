"""
企业注册
"""
from selenium.webdriver.common.by import By

from test_wework.page.base.basepage import BasePage


class Registry(BasePage):
    # def __init__(self,_driver):
    #     self._driver=_driver

    def registry(self, corpname):
        self._driver.find_element(By.ID, 'corp_name').send_keys(corpname)
        # self._driver.find_element(By.CSS_SELECTOR, '.js_corp_industry_text').click()
        # self._driver.find_element(By.ID,'#iagree').click()
        self._driver.find_element(By.ID, 'submit_btn').click()
        return self

    def get_error_message(self):
        result = []
        for element in self._driver.find_elements(By.CSS_SELECTOR, '.js_error_msg'):
            result.append(element.text)
        return result
