class LoginWidget(object):
    def __init__(self, element_base):
        self.element_base = element_base

    def email(self):
        return self.element_base.get_element().element_by_id('email')

    def password(self):
        return self.element_base.get_element().element_by_id('password')

    def login_link(self):
        return self.element_base.get_element().elements_by_css('a')[2]

    def login(self):
        return self.element_base.get_element().element_by_xpath('//*[@id="loginWidget"]/div/div/div/div[2]/button/div/div')