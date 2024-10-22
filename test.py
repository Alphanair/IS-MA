# protocol_codes.py

# Define a dictionary mapping protocol names to their corresponding protocol numbers
protocol_codes = {
    'ICMP': 1,
    'IGMP': 2,
    'GGP': 3,
    'IP': 4,
    'UDP': 17,
    'TCP': 6,
    'ARP': 205,  # Added ARP protocol code
    'EIGRP': 88,
    'OSPF': 89,
    'SCTP': 132,
    'AH': 51,
    'ESP': 50,
    'IPIP': 4,
    'PIM': 103,
    'RIP': 9,
    'GRE': 47,
}

def get_protocol_code(protocol_name):
    """
    Get the protocol code for a given protocol name.

    :param protocol_name: The name of the protocol.
    :return: The corresponding protocol code, or None if not found.
    """
    return protocol_codes.get(protocol_name.upper(), None)

def get_protocol_name(protocol_code):
    """
    Get the protocol name for a given protocol code.

    :param protocol_code: The protocol code.
    :return: The corresponding protocol name, or None if not found.
    """
    for name, code in protocol_codes.items():
        if code == protocol_code:
            return name
    return None
