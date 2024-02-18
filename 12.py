from datetime import datetime
import requests

print(datetime.now())

urls = ["https://github.com",
        "https://github.com",
        "https://github.com"]
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        print(url + " is up")
