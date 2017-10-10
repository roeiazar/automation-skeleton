from src.main.python.com.automation.browser.browser import IBrowserProxy
from selenium import webdriver

from src.main.python.com.automation.utils import Utils


class Chrome(IBrowserProxy):
    def __init__(self): pass

    @Utils.overrides(IBrowserProxy)
    def web_driver(self):
        return webdriver.Chrome('C:/bin/chromedriver.exe')
