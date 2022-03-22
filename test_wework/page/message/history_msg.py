from selenium.webdriver.common.by import By

from test_wework.page.base.basepage import BasePage


class HistoryMsg(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#messageList"

    def history_msg(self):
        elements=self._driver.find_elements(By.CSS_SELECTOR,'msg_history_msgList_td_title ')
        print(elements)



    def get_toast(self):
        content = self.find(By.ID, "js_tips")
        pass
