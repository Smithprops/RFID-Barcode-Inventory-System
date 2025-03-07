import tkinter as tk
from tkinter import messagebox
import requests

SERVER_URL = "http://<micro-pc-ip>:5000"

def scan_rfid():
    rfid = rfid_entry.get()
    response = requests.post(f"{SERVER_URL}/scan_rfid", json={"rfid": rfid})
    messagebox.showinfo("Response", response.json()["message"])

def scan_barcode():
    barcode = barcode_entry.get()
    response = requests.post(f"{SERVER_URL}/scan_barcode", json={"barcode": barcode})
    messagebox.showinfo("Response", response.json()["message"])

root = tk.Tk()
root.title("RFID/Barcode Scanner")
root.geometry("400x300")

tk.Label(root, text="Scan RFID:").pack()
rfid_entry = tk.Entry(root)
rfid_entry.pack()
tk.Button(root, text="Submit RFID", command=scan_rfid).pack()

tk.Label(root, text="Scan Barcode:").pack()
barcode_entry = tk.Entry(root)
barcode_entry.pack()
tk.Button(root, text="Submit Barcode", command=scan_barcode).pack()

root.mainloop()
