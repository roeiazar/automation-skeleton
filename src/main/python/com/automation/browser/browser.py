import abc


class IBrowserProxy():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def web_driver(self):
        pass
