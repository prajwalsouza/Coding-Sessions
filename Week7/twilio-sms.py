from twilio.rest import Client

account_sid = 'ACa573802e1621ce7618faa6d335cc501c'
auth_token = 'the token'

client = Client(account_sid, auth_token)

messageBody = "Hi. I'm sending this from Twilio."
message = client.messages.create(body=messageBody, from_='+12074894215', to='+918904094764')

print(message.sid)
