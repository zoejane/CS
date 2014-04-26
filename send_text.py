from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACd3ac65e1a9f242667b63dfc86ec4f465"
auth_token  = "3cfd4f8bfe32c09486c0feb9d26f36e2"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.sms.messages.create(body="",
    to="+16466279767",    # Replace with your phoe number
#    to="+8613975826861",    # Replace with your phone number
    from_="+12163036608") # Replace with your Twilio number
print message.sid

