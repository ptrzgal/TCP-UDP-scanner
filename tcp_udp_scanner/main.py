import argparse
from scanner.tcp_scan import scan_tcp_ports
from scanner.udp_scan import scan_udp_ports
from scanner.utils import parse_ports

def parse_args():
    parser = argparse.ArgumentParser(description="TCP/UDP Port Scanner")

    parser.add_argument("host", help="IP address or hostname to scan")
    parser.add_argument("-m", "--mode",
                        choices=["TCP", "UDP"],
                        default="TCP",
                        help="Scanning mode: TCP (default) or UDP")
    parser.add_argument("-p", "--ports",
                        help="Port range, such as 20-80 or 22,80,443")
    
    return parser.parse_args()

def main():
    args = parse_args()
    host = args.host
    ports = parse_ports(args.ports)

    if args.mode == "TCP":
        print(f"[+] TCP {host} scanning on ports: {ports}")
        scan_tcp_ports(host, ports)
    elif args.mode == "UDP":
        print(f"[+] UDP {host} scanning on ports: {ports}")
        scan_udp_ports(host, ports)

if __name__ == "__main__":
    main()