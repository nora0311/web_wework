"""
消息群发处理

"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test_wework.page.base.basepage import BasePage
from test_wework.page.message.history_msg import HistoryMsg


class Message(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#/createMessage"

    def send_group_message(self, app="", group="", content=""):
        # 打开 app列表
        self.find(By.LINK_TEXT, "选择需要发消息的应用").click()
        # list,选择要发的 app
        WebDriverWait(self._driver, 10).until(self.wait_element)
        # locator = (By.CSS_SELECTOR, 'div[data-name="两只猫猫"]')
        # self.find(locator).click()

        self.find(By.CSS_SELECTOR, 'div[data-name="%s"]' % app).click()
        # 点击确定
        self.find(By.LINK_TEXT, "确定").click()
        # 发送范围
        self.find(By.LINK_TEXT, "选择发送范围").click()
        # 搜索 这个定位，test_main 里调用可正常运行。test_managetools 调用定位失败
        # self.find(By.ID,'memberSearchInput').send_keys(group)
        # 改为元素，两条用例都运行通过。
        element = self._driver.find_elements(By.CSS_SELECTOR, '.ww_searchInput_text')[-1]
        element.send_keys(group)

        self.find(By.CSS_SELECTOR, '[id="searchResult"] li:nth-child(1)').click()

        self.find(By.LINK_TEXT, "确认").click()
        # 编辑区域
        self.find(By.CSS_SELECTOR, '.js_send_msg_text').send_keys(content)
        # 发送
        self.find(By.LINK_TEXT, "发送").click()
        # 确定发送
        self.find(By.LINK_TEXT, "确定").click()

        # content = self.find(By.ID, "js_tips").text
        return HistoryMsg(reuse=True)

    def wait_element(self, x):
        # 目标元素
        size = len(self._driver.find_elements(By.LINK_TEXT, "确定"))
        if size < 1:
            self._driver.find_element(By.LINK_TEXT, "选择需要发消息的应用").click()
        return size >= 1
