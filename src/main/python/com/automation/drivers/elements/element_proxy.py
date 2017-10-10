import abc


class IElementProxy():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def browser(self):
        pass

    @abc.abstractmethod
    def head(self):
        pass

    @abc.abstractmethod
    def by(self):
        pass

    @abc.abstractmethod
    def elements_by_css(self, selector):
        pass

    @abc.abstractmethod
    def elements_by_tag_name(self, selector):
        pass

    @abc.abstractmethod
    def element_by_xpath(self, selector):
        pass

    @abc.abstractmethod
    def element_by_tag_name(self, selector):
        pass

    @abc.abstractmethod
    def get_children(self, selenium_element):
        pass

    @abc.abstractmethod
    def element_by_cls_name(self, selector):
        pass

    @abc.abstractmethod
    def element_by_id(self, selector):
        pass

    @abc.abstractmethod
    def set_default_timeout(self, default_timeout):
        pass

    @abc.abstractmethod
    def element_by_text(self, text):
        pass

