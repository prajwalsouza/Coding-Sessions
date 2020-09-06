from twilio.rest import Client

account_sid = 'ACa573802e1621ce7618faa6d335cc501c'
auth_token = 'the token'

client = Client(account_sid, auth_token)

call = client.calls.create(twiml='<Response><Say>Hi there. Just testing something.</Say></Response>',from_='+12074894215',to='+918904094764')
print(call.sid)
