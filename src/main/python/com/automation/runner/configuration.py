import getpass

from src.main.python.com.automation.logs.email_notification import EmailNotification


class MainConfig:
    def __init__(self):
        pass

    def setup_scenario(self):
        pass


if __name__ == '__main__':

    try:
        EmailNotification.send_email(getpass.getuser() + " is ready to run automation tests")
    except BaseException:
        pass
