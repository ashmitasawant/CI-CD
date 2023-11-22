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

    # Decode the content from base64
    file_content_base64 = file_info['content']
    file_content_bytes = base64.b64decode(file_content_base64)
    file_content = file_content_bytes.decode('utf-8')

    # Now, 'file_content' contains the content of the file
    print("Content of SnapshotInitial.json:")
    print(file_content)
else:
    print(f"Failed to fetch file. Status code: {response.status_code}")
    print(response.text)
