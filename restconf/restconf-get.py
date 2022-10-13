import json
import requests
requests.packages.urllib3.disable_warnings()
api_url = "https://192.168.56.102/restconf/data/ietf-interfaces:interfaces"
headers = {"Accept":"application/yang-data+json","Content-type":"application/yang-data+json"}
basicauth = ("cisco","cisco123!")
resp=requests.get(api_url,auth=basicauth,headers=headers,verify=False)
json_data = resp.json()
print(json.dumps(json_data,indent=4))