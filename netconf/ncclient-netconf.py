from ncclient import manager
m = manager.connect(
 host="192.168.56.102",
 port=830,
 username="cisco",
 password="cisco123!",
 hostkey_verify=False)