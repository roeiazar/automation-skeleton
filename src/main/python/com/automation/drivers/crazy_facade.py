from src.main.python.com.automation.drivers.editor.default_editor import Editor
from src.main.python.com.automation.drivers.pages.listing_page import ListingPage
from src.main.python.com.automation.drivers.pages.main_page import MainPage


class CrazyFacade(object):
    def __init__(self, element_base):
        self.element_base = element_base

    def main_page(self):
        self.element_base.get_element().head = self.element_base.get_element().element_by_cls_name('page-template-default')
        return MainPage(self.element_base)

    def listing_page(self):
        self.element_base.get_element().head = self.element_base.get_element().element_by_id('app')
        return ListingPage(self.element_base)

    def editor(self):
        self.element_base.get_element().head = self.element_base.get_element().element_by_id('editor-app-wrapper')
        return Editor(self.element_base)

