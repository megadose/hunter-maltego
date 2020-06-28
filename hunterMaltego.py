from MaltegoTransform import *
import json,requests
domain=sys.argv[1]
trx = MaltegoTransform()
apikey="YOUR API KEY"
if apikey=="YOUR API KEY":
    trx.addEntity("maltego.Phrase","Please config the transform with you api key !")
    print(trx.returnOutput())
    exit()
req = requests.get("https://api.hunter.io/v2/domain-search?domain="+domain+"&api_key="+apikey)
data = req.json()["data"]["emails"]
for e in data:
    email = trx.addEntity("maltego.EmailAddress",e["value"])
    email.setLinkLabel("With hunter.io")
print(trx.returnOutput())
