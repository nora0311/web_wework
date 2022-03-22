"""
登录后主界面
"""
from time import sleep

from selenium.webdriver.common.by import By

from test_wework_selenium.page.base.basepage import BasePage
from test_wework_selenium.page.contacts.add_member import AddMemberPage

from test_wework_selenium.page.contacts.import_contact import ImportContact

from test_wework_selenium.page.customer.customer import Customer
from test_wework_selenium.page.manage_tools.managetools import ManageTools
from test_wework_selenium.page.message.message import Message


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    # 添加成员
    def add_member(self):
        self.find(By.LINK_TEXT, '添加成员').click()
        sleep(5)
        # 如果浏览器缩放，处理方法
        # locator = (By.LINK_TEXT, '添加成员')
        # self._driver.execute_script("argument[0].click():",self.find(locator))
        # return Contact(reuse=True)
        return AddMemberPage(reuse=True)

    # 上传处理 导入通讯录
    def import_user_entrance(self):
        self.find(By.CSS_SELECTOR, '.ww_indexImg_Import').click()
        return ImportContact(reuse=True)

    # 主页，常用入口-消息群发
    def send_message(self):
        # 主页-点击消息群发
        # link定位
        self.find(By.LINK_TEXT, "消息群发").click()
        # self.find(By.CSS_SELECTOR,'.js_groupMessage').click()
        return Message(reuse=True)

    # 主页-常用入口-客户联系
    def customer_contact(self):
        self.find(By.LINK_TEXT, "客户联系").click()
        return Customer(reuse=True)

    # 导航部分入口
    # 主页导航，点击管理工具
    def manage_tools(self):
        self.find(By.ID, 'menu_manageTools').click()
        return ManageTools(reuse=True)

    # 验证主体信息，入口跳转
    def goto_authCenter(self):
        # self._driver = webdriver.Chrome()
        self._driver.find_element(By.CSS_SELECTOR, '.js_go_authCenter').click()
