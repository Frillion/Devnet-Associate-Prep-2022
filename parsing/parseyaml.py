# Fill in this file with the code from parsing YAML exercise
<<<<<<< HEAD
=======
import yaml
import json
with open("myfile.yaml",'r') as raw_yaml_data:
    yaml_data = yaml.load(raw_yaml_data)
print(yaml_data)
print("\n\n"+json.dumps(yaml_data,indent = 4))
>>>>>>> 6e8073aea465f70004ac670cdca08f9cc4b5b32a
