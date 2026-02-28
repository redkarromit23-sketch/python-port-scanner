import socket
from threading import Thread
import time

# -------------------------------
# Common Service Ports
# -------------------------------
common_ports = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Proxy"
}

open_ports = []

# -------------------------------
# Scan Function
# -------------------------------
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target_ip, port))

        if result == 0:
            service = common_ports.get(port, "Unknown")
            print(f"[OPEN] Port {port} | Service: {service}")
            open_ports.append((port, service))

        s.close()

    except:
        pass


# -------------------------------
# Main Program
# -------------------------------
print("=" * 45)
print("        PYTHON PORT SCANNER")
print("=" * 45)

target = input("Enter target (IP or Domain): ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid target!")
    exit()

print(f"\nScanning Target: {target_ip}")

start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print("\nScanning started...\n")

start_time = time.time()

threads = []

# Create Threads
for port in range(start_port, end_port + 1):
    t = Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

# Wait for all threads
for t in threads:
    t.join()

end_time = time.time()

# -------------------------------
# Save Results
# -------------------------------
with open("results.txt", "w") as file:
    file.write(f"Scan Results for {target_ip}\n")
    file.write("=" * 30 + "\n")

    for port, service in open_ports:
        file.write(f"Port {port} OPEN | {service}\n")

# -------------------------------
# Final Output
# -------------------------------
print("\nScan Completed!")
print(f"Total Open Ports: {len(open_ports)}")
print(f"Time Taken: {round(end_time - start_time, 2)} seconds")
print("Results saved to results.txt")