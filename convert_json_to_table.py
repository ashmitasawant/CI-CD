import requests
import base64
import json
import os
import json
import csv


api_url = 'https://github.com/ashmitasawant/CI-CD/blob/main/ProcessInfo/SnapshotInitial.json'

response = requests.get(api_url)

# Check if the request was successful (status code 200)
print (response)
data = json.loads(response.read())

# Extract relevant data from the JSON
connection = data["connections"]["connection"][0]
fields = connection["field"]
def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as json_input:
        data = json.load(json_input)

    # Assuming the JSON is a list of dictionaries
    if isinstance(data, list):
        keys = data[0].keys() if data else []
    # Assuming the JSON is a single dictionary
    elif isinstance(data, dict):
        keys = data.keys()
    else:
        raise ValueError("Invalid JSON format")


# Create a CSV file and write the tabular data
with open("table.csv", mode="w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Field ID", "Encrypted Value Set", "Uses Encryption", "Component Override", "Use Default"])

    for field in fields:
        csv_writer.writerow([field["id"], field["encryptedValueSet"], field["usesEncryption"], field["componentOverride"], field["useDefault"]])
