from twilio.rest import Client

# Your Twilio account details
account_sid = "/Users/Razvan/Desktop/IT/keys/twilio_account_sid"
auth_token = "/Users/Razvan/Desktop/IT/keys/twilio_auth_token"
TWILIO_ACCOUNT_SID = open(account_sid, 'r').read().strip()
TWILIO_AUTH_TOKEN = open(auth_token, 'r').read().strip()
twilio_phone_number = "/Users/Razvan/Desktop/IT/keys/twilio_whatsapp_number"
FROM_PHONE = open(twilio_phone_number, 'r').read()
TO_PHONE = ""           # Recepient's Phone Number


# Function to send WhatsApp via Twilio
def send_whatsapp_message(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=message,
        from_ = f"whatsapp:{FROM_PHONE}",  # Twilio WhatsApp number
        to = f"whatsapp:{TO_PHONE}"        # The recipient's WhatsApp number
    )
    print(f"WhatsApp message sent: {message.body}")

# Test message
send_whatsapp_message("Test: WhatsApp message is working!")