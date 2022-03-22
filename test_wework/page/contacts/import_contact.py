from time import sleep

from selenium.webdriver.common.by import By
from test_wework.page.base.basepage import BasePage
from test_wework.page.contacts.contact import Contact


class ImportContact(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts/import_auto/1688851273193684"

    def import_users(self, path):
        # 上传通讯录模板
        self.find(By.ID, 'js_upload_file_input').send_keys(path)
        # 强制等待去掉或者改成显示等待
        sleep(5)
        self.find(By.ID, 'submit_csv').click()
        return Contact(reuse=True)
