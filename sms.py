from twilio.rest import Client
import config
# Your Account SID from twilio.com/console
account_sid = config.config['ac_id']
# Your Auth Token from twilio.com/console
auth_token  = config.config['venus_token']

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16037679057",
    from_="+16033478246",
    body="Hello Venus from Twilio!")

print(message.sid)
