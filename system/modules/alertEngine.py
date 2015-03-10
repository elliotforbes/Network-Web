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
        body="Network Alert - The Network lost it's connectivity, it's back now but further action may be required.",  
    )
    print("Text Alert Successfully sent")
    

def sendThroughputAlert():
    client.messages.create(
        to="+447815497765",
        from_="+441499377047",
        body="Network Alert - Throughput rates are unusually high, please check your network's settings"
    )
    print("Text Alert Successfully sent")
    
    
def sentDownloadAlert():
    client.messages.create(
        to="+447815497765",
        from_="+441499377047",
        body="Network Alert - Download Rates are are unusually low, please check your network's settings"
    )
    print("Text Alert Successfully sent")
    
def senUploadAlert():
    client.messages.create(
        to="+447815497765",
        from_="+441499377047",
        body="Network Alert - Upload Rates are are unusually low, please check your network's settings"
    )
    print("Text Alert Successfully sent")