from src.main.python.com.automation.drivers.crazy_facade import CrazyFacade


class CrazyServices(object):
    @staticmethod
    def facade(element_base):
        return CrazyFacade(element_base)
