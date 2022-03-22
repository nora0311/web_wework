from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_wework.page.base.basepage import BasePage
from test_wework.page.contacts.contact import Contact


class ImportContact(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts/import_auto/1688851273193684"

    def import_users(self, path):
        # 上传通讯录模板
        # self.find(By.ID,'js_upload_file_input').send_keys("/Users/serenehoo/Desktop/PythonProj/auto_test/test_wework_selenium/page/通讯录批量导入模板.xlsx")
        self.find(By.ID, 'js_upload_file_input').send_keys(path)
        # 强制等待去掉或者改成显示等待
        sleep(5)
        # submit_locator=()
        # WebDriverWait(self._driver,10).until(expected_conditions.visibility_of_element_located(submit_locator))
        self.find(By.ID, 'submit_csv').click()
        return Contact(reuse=True)
