import time
from time import sleep

from selenium.webdriver.common.by import By

from test_wework_selenium.page.base.basepage import BasePage


"""
添加员工 page
"""


class AddMemberPage(BasePage):

    def add_member_page(self,name,acctid,phone):
        from test_wework_selenium.page.contacts.contact import Contact
        name_locator = (By.ID, 'username')
        acctid_locator = (By.ID, 'memberAdd_acctid')
        gender_locator = (By.CSS_SELECTOR, '.ww_radio[value="2"]')
        phone_locator = (By.NAME, 'mobile')
        arrow_locator = (By.CSS_SELECTOR, '.ww_telInput_zipCode_input_arrowWrap')
        sleep(5)
        self.find(name_locator).send_keys(name)
        self.find(acctid_locator).send_keys(acctid)
        self.find(gender_locator).click()
        # 手机号
        self.find(arrow_locator).click()
        self.find(By.CSS_SELECTOR, 'li[data-value="886"]').click()
        self.find(phone_locator).send_keys(phone)
        sleep(5)
        self.find(By.LINK_TEXT,'保存').click()

        elements=self._driver.find_elements(By.CSS_SELECTOR, '[placeholder="手机号"]')
        if len(elements)>0:
            self.find(By.CSS_SELECTOR, '[placeholder="手机号"]').send_keys(phone)
            self.find(By.CSS_SELECTOR,'[d_ck="confirm"]').click()
        sleep(5)
        return Contact(reuse=True)


