# 🔍 Advanced Multi-threaded Port Scanner

## 📌 Overview
The **Advanced Multi-threaded Port Scanner** is a high-speed **network scanner** that efficiently detects **open ports** and identifies running **services** on a given target IP. It leverages **multi-threading** to significantly speed up the scanning process, making it much faster than traditional sequential scanners.

## 🚀 Features
✅ **Multi-threaded scanning** – Uses `ThreadPoolExecutor` for high-speed scanning.  
✅ **Custom Port Range** – Allows users to specify **which ports to scan**.  
✅ **Service Detection** – Identifies **services** running on open ports (e.g., `80 → HTTP`).  
✅ **Results Logging** – Saves scan results into a log file (`port_scan_<IP>.txt`).  
✅ **Graceful Exit Handling** – Handles network errors and user interruptions (`Ctrl+C`).  
✅ **Lightweight & Fast** – Minimal dependencies with optimized performance.

---

## 📂 Installation

To run this port scanner, you need **Python 3.x** installed on your system.

### 🛠️ **Step 1: Clone the Repository**
```bash
git clone https://github.com/Rohankoley/PortScanner.git
cd PortScanner
```

### 🛠️ **Step 2: Install Required Dependencies**
```bash
pip install -r requirements.txt
```
📌 **Required Libraries:**  
- `pyfiglet` – For fancy ASCII banners  
- `socket` – For network connections  
- `concurrent.futures` – For multi-threaded scanning  

---

## 🎯 Usage

To run the scanner, execute:

```bash
python port_scanner.py
```

### 📌 Example Run:
 ____            _     ____
|  _ \ ___  _ __| |_  / ___|  ___ __ _ _ __  _ __   ___ _ __ 
| |_) / _ \| '__| __| \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
|  __/ (_) | |  | |_   ___) | (_| (_| | | | | | | |  __/ |   
|_|   \___/|_|   \__| |____/ \___\__,_|_| |_|_| |_|\___|_|   

Target IP: 192.168.1.1
Enter start port: 20
Enter end port: 1000

[OPEN] Port 21: ftp
[OPEN] Port 22: ssh
[OPEN] Port 80: http
[OPEN] Port 443: https

Scanning completed at: 2025-02-19 12:34:56
Total Duration: 0:00:15
```

### 🔧 **Command-line Arguments (Coming Soon!)**
```
python port_scanner.py -t <target_ip> -p <port_range>
```
- `-t` → Target IP Address  
- `-p` → Port range (e.g., `20-1000`)  

---

## 📄 Output
All scan results are **saved in a log file**:
```
port_scan_192.168.1.1.txt
```

---

## 🚀 Future Enhancements
🔹 **UDP Scanning** – Support for UDP port detection  
🔹 **Banner Grabbing** – Fetch service versions running on open ports  
🔹 **GeoIP Lookup** – Identify the target’s physical location  
🔹 **Graphical Interface (GUI)** – Using Tkinter or PyQt  
🔹 **Nmap Integration** – Combine with `nmap` for deeper scanning  

---

## ⚠️ Disclaimer
This tool is for **educational & ethical purposes only**.  
Unauthorized scanning of networks **without permission** is illegal.

---

## 👨‍💻 Author
**Rohan Koley**  
🌐 GitHub: [Rohankoley](https://github.com/Rohankoley)  
