from twilio.rest import Client


class SendMessage:
    def __init__(self):
        self.account_sid = 'AC7ebe55340f19caa0af0b693e1d56f574'
        self.auth_token = 'c6193a3f8ed7a6fb7618ab3e181aefe3'
        self.number = '+19124205814'
        self.client = Client(self.account_sid, self.auth_token)

    def send_sms(self, content):
        message = self.client.messages \
            .create(
                body=content,
                from_=self.number,
                to='+919539537049'
            )
        print(message)
