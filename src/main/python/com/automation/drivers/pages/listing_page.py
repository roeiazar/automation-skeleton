class ListingPage(object):
    def __init__(self, element_base):
        self.element_base = element_base

    def new_listing(self):
        return self.element_base.get_element().element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/a/div/div/span[2]')

    def template(self):
        return self.element_base.get_element().element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div[1]/div/div[2]/div[1]/div/div[1]')

