from twilio.rest import Client
account_sid = "............"
auth_token  = "............"
client = Client(account_sid, auth_token)

my_cell     = "+........."
my_twilio   = "+1........."

client = Client(account_sid, auth_token)

my_msg = "My message here"

message = client.messages.create(to=my_cell, from_=my_twilio, body= my_msg)
#call = client.calls.create(to=my_cell, from_=my_twilio, url="http://demo.twilio.com/docs/voice.xml")
print(message.sid)
# print(call.sid)



