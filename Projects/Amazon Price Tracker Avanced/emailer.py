import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

class Emailer:
    def __init__(self, sender, password):
        self.sender = sender
        self.password = password

    def send_email(self, subject, html_body, to_address):
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.sender
            msg['To'] = to_address
            msg.attach(MIMEText(html_body, 'html'))

            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.login(self.sender, self.password)
                smtp.sendmail(self.sender, to_address, msg.as_string())

            logging.info('Email sent successfully.')

        except Exception as e:
            logging.error(f"Failed to send email: {e}")