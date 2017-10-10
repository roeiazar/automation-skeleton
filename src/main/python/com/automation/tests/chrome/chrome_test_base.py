from src.main.python.com.automation.drivers.elements.element_base import ElementBase
from src.main.python.com.automation.drivers.elements.web_element_proxy import WebElementProxy
from src.main.python.com.automation.tests.general.test_base import TestBase


class ChromeTestBase(TestBase):
    def setUp(self):
        self.element_base = ElementBase(WebElementProxy(None, 'chrome'))
