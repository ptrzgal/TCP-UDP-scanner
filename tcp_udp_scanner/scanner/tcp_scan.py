import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"[TCP] Port {port} open")
    except Exception:
        pass

def scan_tcp_ports(host, ports):
    with ThreadPoolExecutor(max_workers = 100) as executor: # Here you can change how many scans you want to do in parallel
        for port in ports:
            executor.submit(scan_port, host, port)
