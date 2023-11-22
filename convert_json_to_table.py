import requests
import base64
import json
import os
import json
import csv


api_url = 'https://github.com/ashmitasawant/CI-CD/blob/main/ProcessInfo/SnapshotInitial.json'

response = requests.get(api_url)
json_string=json.dumps(response)
# Check if the request was successful (status code 200)
print (response)
data = json.loads(json_string)

# Extract relevant data from the JSON
connection = data["connections"]["connection"][0]
fields = connection["field"]

# Create a CSV file and write the tabular data
with open("table.csv", mode="w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Field ID", "Encrypted Value Set", "Uses Encryption", "Component Override", "Use Default"])

    for field in fields:
        csv_writer.writerow([field["id"], field["encryptedValueSet"], field["usesEncryption"], field["componentOverride"], field["useDefault"]])
