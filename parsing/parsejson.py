# Fill in this file with the code from parsing JSON exercise
import json
import yaml
with open("myfile.json",'r') as raw_json_data:
    json_data = json.load(raw_json_data)
print(json_data)
print("\n\n"+yaml.dump(json_data))
