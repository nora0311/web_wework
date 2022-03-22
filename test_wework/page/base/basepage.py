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
                # 使用已经存在的chrome进程， 命令行执行/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
                options.debugger_address = "127.0.0.1:9222"
                options.add_argument('--ignore-certificate-errors')
                # options.add_experimental_option('w3c', False)
                # options.binary_location="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
                self._driver = webdriver.Chrome(options=options)
            else:
                # 不复用的话，new一个新的 _driver
                self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(5)
        else:
            # login 和 register
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator=""):
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by, locator)
