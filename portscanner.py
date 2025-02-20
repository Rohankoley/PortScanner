import pyfiglet
import sys
import socket
import concurrent.futures
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("Port Scanner")
print(ascii_banner)

target = input("Target IP: ").strip()
start_port = int(input("Enter start port: ").strip())
end_port = int(input("Enter end port: ").strip())

try:
    socket.inet_aton(target)
except socket.error:
    print("❌ Invalid IP Address. Please enter a correct IP!")
    sys.exit()

scan_start_time = datetime.now()
print("\n" + "_" * 60)
print(f"🔍 Scanning Target: {target}")
print(f"🕒 Scan Started at: {scan_start_time}")
print("_" * 60 + "\n")

log_filename = f"port_scan_{target}.txt"

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5)
        result = s.connect_ex((target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port, 'tcp')
            except:
                service = "Unknown Service"
            open_port_info = f"[✅ OPEN] Port {port}: {service}"
            print(open_port_info)
            with open(log_filename, "a", encoding="utf-8") as log_file:
                log_file.write(open_port_info + "\n")
        s.close()
    except Exception as e:
        print(f"[❌ ERROR] Port {port}: {e}")

def multi_threaded_scan(start_port, end_port, max_threads=200):
    with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
        executor.map(scan_port, range(start_port, end_port + 1))

try:
    multi_threaded_scan(start_port, end_port, max_threads=200)
    scan_end_time = datetime.now()
    print("\n" + "_" * 60)
    print(f"✅ Scan Completed at: {scan_end_time}")
    print(f"⏳ Total Duration: {scan_end_time - scan_start_time}")
    print("_" * 60)
    with open(log_filename, "a", encoding="utf-8") as log_file:
        log_file.write(f"\nScan Completed at: {scan_end_time}\n")
        log_file.write(f"Total Duration: {scan_end_time - scan_start_time}\n")

except KeyboardInterrupt:
    print("\n🚪 Exiting...")
    sys.exit()
except socket.error:
    print("\n⚠️ Host not responding... Check network connectivity.")
    sys.exit()
