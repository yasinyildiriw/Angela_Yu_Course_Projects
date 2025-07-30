import smtplib
from twilio.rest import Client

class NotificationManager:

    def __init__(self):
        self.smtp_address = ""
        self.email = ""
        self.email_password = ""
        self.twilio_virtual_number = ""
        self.twilio_verified_number = ""
        self.whatsapp_number = ""
        self.client = Client('', "")
        self.connection = smtplib.SMTP("")

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=self.twilio_virtual_number,
            body=message_body,
            to=self.twilio_verified_number
        )
        print(message.sid)
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{self.whatsapp_number}',
            body=message_body,
            to=f'whatsapp:{self.twilio_verified_number}'
        )
        print(message.sid)

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )
