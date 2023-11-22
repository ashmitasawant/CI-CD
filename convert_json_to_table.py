import os
import json
import csv

file_path = '/ProcessInfo/SnapshotInitial.json'

# Check if the file exists
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        # Read the content of the file
        json_content = json.load(file)
        print("Content of SnapshotInitial.json:")
        print(json.dumps(json_content, indent=2))  # Display formatted JSON content
else:
    print(f"The file {file_path} does not exist.")
