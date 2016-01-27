import os
import sendgrid
from bs4 import BeautifulSoup

class SendGrid(object):
    def __init__(self):
        if (os.environ.get('ENV') != 'prod'):
            self.sg = sendgrid.SendGridClient(os.environ.get('SENDGRID_API_KEY'))
        else:
            self.sg = sendgrid.SendGridClient(os.environ['SENDGRID_API_KEY'])

    def send_email(self, to_email, from_email, subject, body):
        message = sendgrid.Mail()
        message.add_to(to_email)
        message.set_subject(subject)
        soup = BeautifulSoup(body, "html.parser")
        message.set_text(soup.get_text())
        message.set_html(body)
        message.set_from(from_email)
        status, msg = self.sg.send(message)
        return status, msg