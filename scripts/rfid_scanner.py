import requests

SERVER_URL = "http://<micro-pc-ip>:5000"

def scan_rfid(rfid):
    response = requests.post(f"{SERVER_URL}/scan_rfid", json={"rfid": rfid})
    print(response.json())

scan_rfid("1234567890")
