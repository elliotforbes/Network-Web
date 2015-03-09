from twilio.rest import TwilioRestClient 
from private import passwords as pwords
 
# put your own credentials here 
ACCOUNT_SID = pwords.returnAccSID()
AUTH_TOKEN = pwords.returnAuth()
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

def sendAlert():
    client.messages.create(
        to="+447815497765", 
        from_="+441499377047", 
        body="Network Alert - The Network has lost Internet Connectivity",  
    )
    print("Text Alert Successfully sent")
    
sendAlert()