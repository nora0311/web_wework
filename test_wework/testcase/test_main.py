from test_wework.page.base.main import Main


class TestMain:

    def setup(self):
        self.main = Main(reuse=True)

    def test_add_member(self):
        self.main.add_member()

    # 导入通讯录。
    def test_import_users(self):
        # self.main.import_user_entrance().import_users()
        self.main.import_user_entrance().import_users(
            "/Users/serenehoo/Desktop/PythonProj/auto_test/test_wework_selenium/page/通讯录批量导入模板.xlsx")

    def test_send_message(self):
        message = self.main.send_message()
        message.send_group_message(app="两只猫猫", content="content", group="腾讯公司")



    def test_material(self):
        self.main.manage_tools().material(
            "/Users/serenehoo/PycharmProjects/Selenium_pro/test_contact_selenium/testcase/rose.jpg")
