from selenium import webdriver

from src.main.python.com.automation.browser.browser import IBrowserProxy
from src.main.python.com.automation.utils import Utils


class Firefox(IBrowserProxy):
    def __init__(self): pass

    @Utils.overrides(IBrowserProxy)
    def web_driver(self):
        return webdriver.Firefox()
