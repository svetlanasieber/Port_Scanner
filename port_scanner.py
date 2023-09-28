import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} is open")
    sock.close()

def scan_ports(ip, port_range):
    with ThreadPoolExecutor(max_workers=50) as executor:
        for port in port_range:
            executor.submit(scan_port, ip, port)

if __name__ == "__main__":
    target_ip = "127.0.0.1"  # Replace with the IP you want to scan
    target_ports = range(20, 1024)  # Ports range to scan

    print(f"Scanning ports for IP {target_ip}...")
    scan_ports(target_ip, target_ports)
