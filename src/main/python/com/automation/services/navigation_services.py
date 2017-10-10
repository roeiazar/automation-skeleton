class NavigationServices(object):
    @staticmethod
    def go_to(element_base, url):
        element_base.get_element().browser().get(url)
