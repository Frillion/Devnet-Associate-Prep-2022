# Fill in this file with the code from parsing YAML exercise
import yaml
import json
with open("myfile.yaml",'r') as raw_yaml_data:
    yaml_data = yaml.load(raw_yaml_data)
print(yaml_data)
print("\n\n"+json.dumps(yaml_data,indent = 4))
