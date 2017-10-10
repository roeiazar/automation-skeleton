from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.main.python.com.automation.browser.setup.chrome import Chrome
from src.main.python.com.automation.browser.setup.firefox import Firefox
from src.main.python.com.automation.drivers.elements.element_proxy import IElementProxy


class WebElementProxy(IElementProxy):
    def __init__(self, head, browser_name):
        if browser_name == 'firefox':
            firefox = Firefox()
            self.web_driver = firefox.web_driver()
        else:
            chrome = Chrome()
            self.web_driver = chrome.web_driver()

        if head is not None:
            self.head = head

        self.web_driver.set_page_load_timeout(60)
        self.default_timeout = 10

    def browser(self):
        return self.web_driver

    def head(self):
        return self.web_driver.find_elements_by_css_selector('html')

    def by(self):
        return By

    def elements_by_css(self, selector):
        return self.__elements(self.by().CSS_SELECTOR, selector)

    def elements_by_tag_name(self, selector):
        return self.__elements(self.by().TAG_NAME, selector)

    def element_by_tag_name(self, selector):
        return self.__element(self.by().TAG_NAME, selector)

    def element_by_cls_name(self, selector):
        return self.__element(self.by().CLASS_NAME, selector)

    def element_by_id(self, selector):
        return self.__element(self.by().ID, selector)

    def element_by_xpath(self, selector):
        return self.__element(self.by().XPATH, selector)

    def element_by_text(self, text):
        return self.web_driver.find_elements_by_link_text(text)[0]

    def set_default_timeout(self, default_timeout):
        self.default_timeout = default_timeout

    def get_children(self, selenium_element):
        return selenium_element.find_elements_by_css_selector('*')

    def __element(self, by, selector):
        return WebDriverWait(self.web_driver, self.default_timeout).until(
            EC.presence_of_element_located((by, selector)))

    def __elements(self, by, selector):
        self.__element(by, selector)
        return self.browser().find_elements(by, selector)
