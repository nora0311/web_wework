"""
主页-管理工具
"""
from selenium.webdriver.common.by import By

from test_wework.page.base.basepage import BasePage
from test_wework.page.manage_tools.material import Material
from test_wework.page.manage_tools.staff_service import StaffService
from test_wework.page.message.message import Message


class ManageTools(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#manageTools"

    # 素材库
    def goto_material(self):
        # 点击素材库
        material_locator = (
            By.CSS_SELECTOR, '[id="js_manageTools_index"] li:nth-child(5) .manageTools_cnt_item_desc_title')
        self.find(material_locator).click()
        return Material(reuse=True)

    # 进入消息群发
    def send_message(self):
        # 管理工具-消息群发
        self.find(By.CSS_SELECTOR,
                  '[id="js_manageTools_index"] li:nth-child(3) .manageTools_cnt_item_desc_title').click()
        return Message(reuse=True)

    # 进入员工服务
    def staff_service(self):
        staff_locator=(By.CSS_SELECTOR,'[id="js_manageTools_index"] li:nth-child(6) .manageTools_cnt_item_desc_title')
        self.find(staff_locator).click()
        return StaffService(reuse=True)




