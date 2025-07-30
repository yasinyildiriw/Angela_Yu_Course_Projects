from twilio.rest import Client

class NotificationManager:

    def __init__(self):
        self.client = Client("","")

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_="",
            body=message_body,
            to=""
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{""}',
            body=message_body,
            to=f'whatsapp:{""}'
        )
        print(message.sid)