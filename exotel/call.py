from exotel import Exotel 
import json
import requests
'''
client = Exotel('non56','eedaef1428bfc46e254134be41cd5380b85ccc56')




x  = client.call_flow(from_num,call_id,(56743))
print x

data = json.loads(x.content)
print data["Call"]["PhoneNumberSid"]
'''

base = "https://non56:eedaef1428bfc46e254134be41cd5380b85ccc56@twilix.exotel.in/v1/Accounts/non56/Calls/connect"
from_num = "%011d"% (9560894192) 
call_id  = "%011d"% (9243422233)
data = {
            'From': from_num,
            'CallerId': call_id,
            'Url': "http://my.exotel.in/exoml/start/56743",
            'StatusCallback':'http://localhost:5000/calldata'
        }

x  = requests.post(base,data)
print x