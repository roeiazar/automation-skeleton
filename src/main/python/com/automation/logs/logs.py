import getpass
import os


class WriteLogToFile:
    def __init__(self):
        self._directory = "/Users/" + getpass.getuser() + "/automation_log/"
        if not os.path.exists(self._directory):
            os.makedirs(self._directory)

    def log(self, message):
        f = open(self._directory + "/log.log", 'a+')
        f.writelines(message + "\n")
        print(message)
