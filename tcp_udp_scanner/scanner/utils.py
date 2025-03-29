def parse_ports(ports_str):
    ports = set()
    parts = ports_str.split(',')

    for part in parts:
        if '-' in part:
            start, end = part.split('-')
            ports.update(range(int(start), int(end) + 1))
        else:
            ports.add(int(part))

    return sorted(ports)
