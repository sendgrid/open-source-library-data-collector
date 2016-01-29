import os
import sendgrid
from bs4 import BeautifulSoup


class SendGrid(object):
    """Send an email through SendGrid"""
    def __init__(self):
        if (os.environ.get('ENV') != 'prod'):  # We are not in Heroku
            sendgrid_api_key = os.environ.get('SENDGRID_API_KEY')
        else:
            sendgrid_api_key = os.environ['SENDGRID_API_KEY']
        self.sg = sendgrid.SendGridClient(sendgrid_api_key)

    def send_email(self, to_email, from_email, subject, body):
        """Send the email

                :param to_email:   who the email is going to
                                   (e.g. 'First Last <email@example.com>')
                :param from_email: who the email is coming from
                                   (e.g. 'First Last <email@example.com>')
                :param subject:    the email subject line
                :param body:       the email body in HTML format
                :type to_email:    string
                :type from_email:  string
                :type subject:     string
                :type body:        string

                :returns: HTML status code and JSON message from SendGrid's API
                :rtype: Integer, JSON
        """
        message = sendgrid.Mail()
        message.add_to(to_email)
        message.set_subject(subject)
        message.set_html(body)
        soup = BeautifulSoup(body, "html.parser")
        message.set_text(soup.get_text())
        message.set_from(from_email)
        status, msg = self.sg.send(message)
        return status, msg
