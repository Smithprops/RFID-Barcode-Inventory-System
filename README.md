# 📌 RFID & Barcode Inventory System
### **Efficient Tool & Equipment Tracking with RFID/NFC & Barcodes**

[![GitHub Repo](https://img.shields.io/github/stars/Smithprops/RFID-Barcode-Inventory-System?style=social)](https://github.com/Smithprops/RFID-Barcode-Inventory-System)
[![License](https://img.shields.io/github/license/Smithprops/RFID-Barcode-Inventory-System)](LICENSE)

---

## **📖 Overview**
The **RFID & Barcode Inventory System** is designed to efficiently track and manage tools, equipment, or inventory using **RFID/NFC badges for user authentication** and **barcodes for item tracking**. This system consists of:

- A **Micro PC** that acts as the **master server**, running the backend and database.
- A **Raspberry Pi client** that handles **RFID scanning, barcode scanning, and touchscreen UI**.

This system helps ensure **secure access**, **accurate inventory tracking**, and **simplified checkout/return processes**.

---

## **🚀 Features**
✅ **RFID/NFC Authentication** – Users scan RFID badges to check out items.  
✅ **Barcode-Based Inventory** – Tools and equipment are identified via barcodes.  
✅ **Flask Backend** – Manages users, inventory, and transactions.  
✅ **PostgreSQL Database** – Stores tool checkouts and returns.  
✅ **Redis Caching & Logging** – Improves performance and logs scans.  
✅ **React Admin Dashboard** – Provides a user-friendly web interface.  
✅ **Raspberry Pi Client** – Runs a touchscreen interface for scanning.  
✅ **Docker Support** – Simple deployment with `docker-compose`.  
✅ **Auto-Start on Raspberry Pi** – Runs automatically on boot.  

---

## **📁 Project Structure**
```
rfid_inventory_system/
├── backend/
│   ├── app.py              # Flask backend API
│   ├── models.py           # Database models
│   ├── config.py           # Configuration settings
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Backend containerization
│
├── frontend/
│   ├── src/
│   │   ├── App.js          # React front-end
│   │   ├── components/     # Reusable React components
│   │   ├── pages/          # Dashboard pages
│   ├── public/
│   ├── package.json        # React dependencies
│   ├── Dockerfile          # Frontend containerization
│
├── scripts/
│   ├── rfid_scanner.py     # Python script for RFID scanning
│   ├── barcode_scanner.py  # Python script for Barcode scanning
│   ├── client.py           # Raspberry Pi client script
│   ├── gui.py              # Touchscreen GUI for Raspberry Pi
│
├── docker-compose.yml       # Docker Compose setup
├── README.md                # Project documentation
```

---

## **🛠️ Setup & Installation**
### **1️⃣ Install Dependencies**
#### **Micro PC (Master Server)**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install docker.io docker-compose postgresql redis-server
```

#### **Raspberry Pi (Client)**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip
pip3 install requests opencv-python pyzbar serial
```

---

### **2️⃣ Clone or Download the System**
#### **Using GitHub:**
```bash
git clone https://github.com/Smithprops/RFID-Barcode-Inventory-System.git
cd RFID-Barcode-Inventory-System
```
#### **Or download the ZIP file**, extract it, and navigate to the project directory.

---

### **3️⃣ Start the System on the Micro PC**
```bash
docker-compose up --build
```
- **Backend API:** `http://<micro-pc-ip>:5000`
- **Admin Dashboard:** `http://<micro-pc-ip>:3000`

---

### **4️⃣ Run the Raspberry Pi Client**
```bash
python3 scripts/client.py
```
Or launch the **Touchscreen UI:**
```bash
python3 scripts/gui.py
```

---

### **5️⃣ Configure Auto-Start on Boot (Raspberry Pi)**
To ensure the scanner runs automatically on startup:
```bash
sudo nano /etc/rc.local
```
Add this line **before** `exit 0`:
```bash
python3 /home/pi/RFID-Barcode-Inventory-System/scripts/client.py &
```
Save and reboot:
```bash
sudo reboot
```

---

## **📊 Usage Instructions**
### **🔹 Checking Out a Tool**
1. **User scans their RFID badge**.
2. **User scans the barcode of the tool**.
3. **System logs the transaction** in the database.

### **🔹 Returning a Tool**
1. **User scans their RFID badge again**.
2. **User scans the barcode of the tool to return it**.
3. **System updates the tool status to "Available"**.

---

## **📌 Next Steps**
📌 **Test the system** on both Micro PC and Raspberry Pi.  
📌 **Customize the admin panel** for your needs.  
📌 **Enable alerts** for overdue tools (optional).  
📌 **Request additional features** if needed!  

---

## **📝 License**
This project is **open-source** and available under the [MIT License](LICENSE).

---

## **🤝 Contributing**
Contributions are welcome!  
Feel free to submit issues, pull requests, or suggestions.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Added a new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a **Pull Request**.

---

## **📞 Support**
For issues or feature requests, open a GitHub **Issue** or contact us via [GitHub Discussions](https://github.com/Smithprops/RFID-Barcode-Inventory-System/discussions).

---

### **🚀 Ready to Get Started?**
Clone the repo, follow the setup guide, and deploy your own **RFID & Barcode Inventory System** today!  
