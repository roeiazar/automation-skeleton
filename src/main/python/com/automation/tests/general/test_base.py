import unittest

from src.main.python.com.automation.services.tabs_and_windows_services import TabsAndWindowsServices


class TestBase(unittest.TestCase):
    def tearDown(self):
        TabsAndWindowsServices.browser(self.element_base).close()
