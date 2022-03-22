"""
url https://work.weixin.qq.com/
未登录页面，测试注册。
注册成功
注册失败

"""
from test_wework.page.login.index import Index


class TestIndex:
    def setup(self):
        # self._driver = webdriver.Chrome()
        # self._driver.get("https://work.weixin.qq.com/")
        # self._driver.implicitly_wait(5)
        self.index = Index()

    def test_register(self):
        # main-立即注册
        self.index.goto_register().registry("霍格沃茨")

    def test_login(self):
        register_page = self.index.goto_login().goto_register().registry("ceceshi")

        assert "请选择" in "|".join(register_page.get_error_message())
