import os
import sendgrid
from sendgrid.helpers.mail import *
from bs4 import BeautifulSoup


class SendGrid(object):
    """Send an email through SendGrid"""
    def __init__(self):
        if (os.environ.get('ENV') != 'prod'):  # We are not in Heroku
            sendgrid_api_key = os.environ.get('SENDGRID_API_KEY')
        else:
            sendgrid_api_key = os.environ['SENDGRID_API_KEY']
        self.sg = sendgrid.SendGridAPIClient(apikey=sendgrid_api_key)

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
        from_email = Email(from_email)
        subject = subject
        to_email = Email(to_email)
        soup = BeautifulSoup(body, "html.parser")
        content = Content("text/plain", soup.get_text())
        mail = Mail(from_email, subject, to_email, content)
        response = self.sg.client.mail.send.post(request_body=mail.get())

        return response.status_code, response.body
