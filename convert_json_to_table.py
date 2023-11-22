import requests
import json
import csv

def download_json(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for errors
    return response.json()

def json_to_csv(json_data, csv_file):
    if isinstance(json_data, list):
        keys = json_data[0].keys() if json_data else []
    elif isinstance(json_data, dict):
        keys = json_data.keys()
    else:
        raise ValueError("Invalid JSON format")

    # with open(csv_file, 'w', newline='') as csv_output:
    #     writer = csv.DictWriter(csv_output, fieldnames=keys)
    #     writer.writeheader()

    #     if isinstance(json_data, list):
    #         writer.writerows(json_data)
    #     elif isinstance(json_data, dict):
    #         writer.writerow(json_data)

    # Create a CSV file and write the tabular data
    with open(csv_file, mode="w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Field ID", "Encrypted Value Set", "Uses Encryption", "Component Override", "Use Default"])
    
        for field in fields:
            csv_writer.writerow([field["id"], field["encryptedValueSet"], field["usesEncryption"], field["componentOverride"], field["useDefault"]])


if __name__ == "__main__":
    # Replace 'https://example.com/data.json' with your actual URL
    json_url =  'https://github.com/ashmitasawant/CI-CD/blob/main/ProcessInfo/SnapshotInitial.json'
    
    # Replace 'output.csv' with your desired CSV file name
    csv_file_path = 'output.csv'

    
    json_data = download_json(json_url)

    # Convert JSON to CSV
    json_to_csv(json_data, csv_file_path)

    print(f"Conversion successful. CSV file saved at {csv_file_path}")


