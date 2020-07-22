import clx
import time
from twilio.rest import Client

def sendSMS(user_phone):
# Your Account SID from twilio.com/console
        account_sid = "ACe093788c76cdbb56cf3741ee4ca25649"
# Your Auth Token from twilio.com/console
        auth_token  = "544fac9cfc53aebc3f63bbbb5d67ff97"

        client = Client(account_sid, auth_token)
        # converting entered number to string
        number = str(user_phone)
        print("The phone number entered is {}".format(number))
        print("Adding country code +91 to the number")
        print('+91'+ number)
        message = client.messages.create(
        to="+91"+ number,
        from_="+19564508912",
        body="Reminder from Finbot")

        print(message.sid)



