class ElementBase(object):
    def __init__(self, element_proxy):
        self.element_proxy = element_proxy

    def get_element(self):
        return self.element_proxy
