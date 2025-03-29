import socket
from concurrent.futures import ThreadPoolExecutor

def scan_udp_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(1)
            s.sendto(b'', (host, port))
            try:
                data, _ = s.recvfrom(1024)
                print(f"[UDP] Port {port} open (a reply was received)")
            except socket.timeout:
                print(f"[UDP] Port {port} may be open (no answer)")
    except Exception:
        pass

def scan_udp_ports(host, ports):
    with ThreadPoolExecutor(max_workers = 100) as executor: # Here you can change how many scans you want to do in parallel
        for port in ports:
            executor.submit(scan_udp_port, host, port)
