import json
import csv

json_data = """
{  # Paste your JSON data here
  "@type": "EnvironmentExtensions",
  "connections": {
    "@type": "Connections",
    "connection": [
      {
        "@type": "Connection",
        "field": [
          {
            "@type": "Field",
            "id": "authType",
            "encryptedValueSet": false,
            "usesEncryption": false,
            "componentOverride": false,
            "useDefault": true
          },
          {
            "@type": "Field",
            "id": "oauthOptions/OAuth2Config/credentials/@clientId",
            "encryptedValueSet": false,
            "usesEncryption": false,
            "componentOverride": false,
            "useDefault": true
          },
          {
            "@type": "Field",
            "id": "oauthOptions/OAuth2Config/credentials/@clientSecret",
            "encryptedValueSet": false,
            "usesEncryption": false,
            "componentOverride": false,
            "useDefault": true
          },
          {
            "@type": "Field",
            "id": "oauthOptions/OAuth2Config/credentials/@accessToken",
            "encryptedValueSet": false,
            "usesEncryption": true,
            "componentOverride": false,
            "useDefault": true
          }
        ],
        "id": "4d3f80eb-5a5e-421e-b596-c5a56e739607",
        "name": "Boomi_Service_Slack_Connector"
      }
    ]
  },
  "environmentId": "b8ece4bb-0306-45dc-8911-c31dd6e11d14",
  "extensionGroupId": "",
  "id": "b8ece4bb-0306-45dc-8911-c31dd6e11d14"
}
"""

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
