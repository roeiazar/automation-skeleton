import unittest


from src.main.python.com.automation.services.crazy_services import CrazyServices
from src.main.python.com.automation.services.navigation_services import NavigationServices
from src.main.python.com.automation.tests.chrome.chrome_test_base import ChromeTestBase


class LoginTest(ChromeTestBase):
    def setUp(self):
        super().setUp()
        self.facade = CrazyServices.facade(self.element_base)

    def test_login(self):
        NavigationServices.go_to(self.element_base, "https://crazylister.com")

        main_page = self.facade.main_page()
        main_page.login().click()
        login_widget = self.facade.main_page().login_widget()
        if login_widget.login_link().is_displayed():
            login_widget.login_link().click()

        login_widget.email().send_keys("roei.azar@gmail.com")
        login_widget.password().send_keys("123456789")
        login_widget.login().click()


if __name__ == "__main__":
    unittest.main()
