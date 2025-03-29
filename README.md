# TCP-UDP-scanner
Simple TCP/UDP port scanner written in Python.

## Features
- TCP and UDP port scanning
- Support for port ranges and lists (e.g. `-p 20-25,80,443`)
- Threads for faster scanning

## Requirements
- Python 3.7+

## Getting started

```bash
# Example: TCP scanning
python3 main.py scanme.nmap.org -m TCP -p 22,80

# Example: UDP scanning
python3 main.py 127.0.0.1 -m UDP -p 53,123
```
## Terms of Use

- Do not scan hosts without the express permission of the owner.
- The tool is for educational purposes and testing in a secure environment only.
- Official test host provided by Nmap developers: [https://scanme.nmap.org](https://scanme.nmap.org)

> Use in moderation - scanning multiple ports or frequent requests may be considered abuse.