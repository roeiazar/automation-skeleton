import smtplib


class EmailNotification(object):
    to = ['roei.azar@gmail.com']
    subject = 'Automation Report'

    @staticmethod
    def send_email(body):
        try:
            message = f'Subject: {subject}\n\n{body}'
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login('roei.azar@gmail.com', '###')
            server.sendmail('roei.azar@gmail.com', '', message)
            server.close()

        except BaseException as e:
            print('Something went wrong...\n' + e.message)
