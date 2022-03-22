"""
使用复用浏览器方法
"""

from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _driver = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None, reuse=False):

        if driver is None:
            if reuse is True:
                options = webdriver.ChromeOptions()
                options.debugger_address = "127.0.0.1:9222"
                # options.add_argument('--ignore-certificate-errors')
                # options.add_experimental_option('w3c', False)
                self._driver = webdriver.Chrome(options=options)
            else:
                # 不复用浏览器
                self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator=""):
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by, locator)
