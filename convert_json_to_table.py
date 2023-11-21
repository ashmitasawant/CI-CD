import os
import json
import csv

json_data = os.environ.get("extensions_json")
print ($json_data)
data = json.loads(json_data)

# Extract relevant data from the JSON
connection = data["connections"]["connection"][0]
fields = connection["field"]

# Create a CSV file and write the tabular data
with open("table.csv", mode="w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Field ID", "Encrypted Value Set", "Uses Encryption", "Component Override", "Use Default"])

    for field in fields:
        csv_writer.writerow([field["id"], field["encryptedValueSet"], field["usesEncryption"], field["componentOverride"], field["useDefault"]])
