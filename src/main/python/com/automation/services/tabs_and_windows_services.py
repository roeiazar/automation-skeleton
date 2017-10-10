class TabsAndWindowsServices(object):
    @staticmethod
    def switch_to_main_window(element_base):
        main_window = element_base.get_element().browser().current_window_handle
        element_base.get_element().browser().switch_to.window(main_window)

    @staticmethod
    def browser(element_base):
        return element_base.get_element().browser()
