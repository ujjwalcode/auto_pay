# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "ACa6d4cb06b269945f34462a435110511f"
auth_token = "4c74480dcf8daab2fc8a078e5ca40d43"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+917610002521", from_="+13176224171",
                                     body="you have selected autopay next time you can pay automatically via calling to TOLL FREE no. 1800 1234 5678 ")