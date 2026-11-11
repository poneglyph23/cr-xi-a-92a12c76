def parse_port(value):
    """Parse a port number or a known service alias."""
    aliases = {}
    if value in aliases:
        return aliases[value]
    port = int(value)
    if not 0 < port < 65536:
        raise ValueError("port out of range")
    return port
