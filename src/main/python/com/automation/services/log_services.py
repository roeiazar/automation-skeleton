from src.main.python.com.automation.logs.logs import WriteLogToFile


class LogServices(object):
    @staticmethod
    def element_not_clickable(element):
        print("Element is not clickable: #id", element.id)

    @staticmethod
    def write_log_to_file(message):
        WriteLogToFile().log(message)
