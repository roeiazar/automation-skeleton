class Editor(object):
    def __init__(self, element_base):
        self.element_base = element_base

    def global_controls(self):
        return self.element_base.get_element().element_by_id('global-controls')