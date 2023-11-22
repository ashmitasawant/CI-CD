import requests
from base64 import b64decode

def file_content():
    url = f'https://github.com/ashmitasawant/CI-CD/blob/main/ProcessInfo/SnapshotInitial.json'
    response = requests.get(url)

    if response.status_code == 200:
        content = response.json().get('content')
        if content:
            with open("demo.txt","w") as fp:
                fp.write(b64decode(content).decode('utf-8'))
            return "hello"
        else:
            print("Content not found ")
    else:
        print(f"Status code: {response.status_code}")

    return None


file_content = file_content()

if file_content is not None:
    print(file_content)
