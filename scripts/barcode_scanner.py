import requests

SERVER_URL = "http://<micro-pc-ip>:5000"

def scan_barcode(barcode):
    response = requests.post(f"{SERVER_URL}/scan_barcode", json={"barcode": barcode})
    print(response.json())

scan_barcode("ABC123")
