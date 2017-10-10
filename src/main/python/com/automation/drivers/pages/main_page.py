from src.main.python.com.automation.drivers.widgets.login_widget import LoginWidget


class MainPage(object):
    def __init__(self, element_base):
        self.element_base = element_base

    def login_widget(self):
        self.element_base.get_element().head = self.element_base.get_element().element_by_id('loginWidget')
        return LoginWidget(self.element_base)

    def login(self):
        return self.element_base.get_element().element_by_text('Login')
