from twilio.rest import Client


account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
twilio_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'
your_phone_number = 'YOUR_PHONE_NUMBER_TO_RECEIVE_NOTIFICATIONS'

def send_text(new_items):
    client = Client(account_sid, auth_token)
    for key in new_items.keys():
        message_body = f'New item on sale: {key}\nCheck it out: {new_items[key]}'
        message = client.messages.create(
            body = message_body,
            from_ = twilio_phone_number,
            to = your_phone_number
        )