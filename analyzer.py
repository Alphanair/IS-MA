# main.py

from scapy.all import sniff, ARP, Ether, IP, TCP, UDP, Raw
from test import get_protocol_code, get_protocol_name

def packet_callback(packet):
    try:
        # Check for ARP layer
        if packet.haslayer(ARP):
            arp_layer = packet[ARP]
            print(f"ARP Packet: {packet.summary()}")
            print(f"Source MAC: {arp_layer.hwsrc}")
            print(f"Source IP: {arp_layer.psrc}")
            print(f"Destination MAC: {arp_layer.hwdst}")
            print(f"Destination IP: {arp_layer.pdst}")
            print("-" * 50)

        # Check for IP layer
        elif packet.haslayer(IP):
            ip_layer = packet[IP]
            protocol = ip_layer.proto
            
            # Display packet information
            print(f"Packet: {packet.summary()}")
            print(f"Source IP: {ip_layer.src}")
            print(f"Destination IP: {ip_layer.dst}")
            print(f"Protocol: {protocol}")
            
            # If there's a payload, show it
            if packet.haslayer(Raw):
                raw_layer = packet[Raw]
                print(f"Payload: {raw_layer.load}")

            print("-" * 50)

    except Exception as e:
        print(f"Error processing packet: {e}")

def main():
    # Set the interface to capture packets from (change as needed)
    interface = "Wi-Fi"  # Change to your network interface
    print(f"Capturing packets on interface: {interface}")
    
    # Start packet capture
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
