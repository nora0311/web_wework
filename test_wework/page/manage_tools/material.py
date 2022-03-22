"""
素材库界面

"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from test_wework.page.base.basepage import BasePage


class Material(BasePage):
    # 图片类型
    def pic_material(self, filepath):
        # 切换到图片
        # 可以用 link text,css
        # self.find(By.CSS_SELECTOR, '[id="profile_navigation"] li:nth-child(3) .ww_icon_GrayPic').click()
        self.find(By.LINK_TEXT, "图片").click()
        # 点击添加图片
        self.find(By.CSS_SELECTOR, '.js_upload_file_selector').click()
        # 添加图片
        self.find(By.ID, 'js_upload_input').send_keys(filepath)
        sleep(5)
        # 完成
        self.find(By.CSS_SELECTOR, '.js_next').click()
        element: WebElement = self.find(By.ID, 'js_upload_input')
        return self

    def text_material(self, content=""):
        # 切换到文字
        self.find(By.LINK_TEXT, "文字").click()
        self.find(By.LINK_TEXT, "添加文字").click()
        self.find(By.CSS_SELECTOR, '.js_text_content').send_keys(content)
        WebDriverWait(self._driver, 10).until(self.wait_element)
        # self.find(By.LINK_TEXT, "选择").click
        self.find(By.CSS_SELECTOR, '.appPermissionDlg_listWrap label:nth-child(3) .ww_checkbox').click()
        # # 点击确定
        self.find(By.LINK_TEXT, "确定").click()
        self.find(By.LINK_TEXT, "保存").click()

    def wait_element(self, x):
        size = len(self._driver.find_elements(By.CSS_SELECTOR, '.appPermissionDlg_listWrap .ww_checkbox'))
        if size < 1:
            self._driver.find_element(By.LINK_TEXT, "选择").click()
        return size >= 3

    def del_text_material(self):
        pass

    def mix_material(self):
        pass

    def voice_material(self):
        pass

    def video_material(self):
        pass

    def file_material(self):
        pass
