import requests
import urllib.parse
host_name = "mapquestapi.com/"
route = "directions/v2/route?"
origin = "Rome, Italy"
destination = "Frascati, Italy"
key = "Uu9fN5w1tQ0hLb3g4zPeILzGEbMck6OD"
parameters = urllib.parse.urlencode({"key":key,"from":origin,"to":destination,"outFormat":"json"})
full_api = f"https://www.{host_name}{route}{parameters}"
json_data = requests.get(full_api).json()
print(json_data)
