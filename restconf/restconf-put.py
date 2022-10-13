import json
import requests
requests.packages.urllib3.disable_warnings()
api_url = "https://192.168.56.102/restconf/data/ietf-interfaces:interfaces/interface=Loopback1"
headers = { "Accept":"application/yang-data+json",
            "Content-Type":"application/yang-data+json"}
basicauth=("cisco","cisco123!")
yangConfig={
    "ietf-interfaces:interface":{
        "name":"Loopback1",
        "description":"The First Loopback Interface",
        "type":"iana-if-type:softwareLoopback",
        "enabled":True,
        "ietf-ip:ipv4":{"address":[{"ip":"10.1.1.1","netmask":"255.255.255.0"}]},
        "ietf-ip:ipv6":{}
    }
}
resp = requests.put(api_url,data=json.dumps(yangConfig),auth=basicauth,headers=headers, verify=False)
if(resp.status_code >=200 and resp.status_code <= 299):
    print("Status Success:{}".format(resp.status_code))
else:
    print("Error. Status Failure: {} \Error message: {}".format(resp.status_code,resp.json()))
