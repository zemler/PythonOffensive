import requests
import sys

keywords = ["password", "secret", "db_password", "test"] #Modify it
app_url = sys.argv[1]

def secret_finder(app_url, keywords):
    req = requests.get(app_url)
    content = req.text.lower()
    for keyword in keywords:
        if keyword.lower() in content:
            print(f"[+] Keyword: {keyword} Found!")

if __name__ == "__main__":
    secret_finder(app_url, keywords)