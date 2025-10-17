import requests
import time

URL = "https://www.mcserverhost.com/api/servers/94bf2cef/subscription"
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*"
}

while True:
    try:
        r = requests.post(URL, headers=HEADERS)
        print(f"[+] Status: {r.status_code} | Response: {r.text}")
    except Exception as e:
        print(f"[!] Error: {e}")
    time.sleep(10)
