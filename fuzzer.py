# Very Very Simple API fuzzer 
import requests
import sys

adress = sys.argv[1]
dictionary = sys.argv[2]

with open(dictionary, "r") as file:
    while True:
        name = file.readline().strip()
        if name == '':
            break
        
        #Change if u need to use http://:
        req = requests.get(url=f"https://{adress}/{name}")
        print(f"{name} STATUS CODE: {req.status_code}")
