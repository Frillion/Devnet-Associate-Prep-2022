import requests
import urllib.parse
host_name = "mapquestapi.com/"
route = "directions/v2/route?"
key = "Uu9fN5w1tQ0hLb3g4zPeILzGEbMck6OD"
while True:
    origin = input("Starting Location: ")
    if origin == "quit" or origin == "q":
        break
    destination = input("Destination: ")
    if destination == "quit" or destination == "q":
        break
    parameters = urllib.parse.urlencode({"key":key,"from":origin,"to":destination,"outFormat":"json"})
    full_api = f"https://www.{host_name}{route}{parameters}"
    json_data = requests.get(full_api).json()
    print("URL: "+full_api)
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print(f"Api Status:{json_status}- A successful route call\n")
