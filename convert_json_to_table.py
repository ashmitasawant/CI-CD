import requests
import base64
import json
import os
import json
import csv


api_url = 'https://github.com/ashmitasawant/CI-CD/blob/main/ProcessInfo/SnapshotInitial.json'

response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    file_info = response.json()


    # Now, 'file_content' contains the content of the file
    print("Content of SnapshotInitial.json:")
    print(file_content)
else:
    print(f"Failed to fetch file. Status code: {response.status_code}")
    print(response.text)
