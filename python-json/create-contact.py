import json
import os
import requests

#config File
#with open("local_env.json", "r") as f:
#    conf_file = f.read()
#    config = json.loads(conf_file)

#for value in config["values"]:
    #value["key"] = value["value"]
    #print(value["key"])


# Convert Postman collection to Python script
with open('Collections/test-collection.json') as f:
    data = json.load(f)

for item in data['collection']['item']:
    # Extract request details
    request = item['request']
    url = request['url']['raw']
    method = request['method']
    headers = request['header']

    #if not request:
    data = request['body']['raw']
    
    
    #print(url)
    #exit()

    # Generate Python code
    response = requests('{url}', headers={headers}, data='{data}')
    print(response)


# Load the Postman collection JSON file
#with open('local_env.json', 'r') as f:
#    environment = json.load(f)

# Get the values of the environment variables
#environment["key"] = environment['values'][0]['value']
#environment["key"] = environment['values'][1]['value']

#for value in environment["values"]:
#    environment["key"] = value["value"]
#    print(environment["key"])

# Print the values of the environment variables
#print('Local variable value:', variable_1)
#print('Global variable value:', variable_2)
