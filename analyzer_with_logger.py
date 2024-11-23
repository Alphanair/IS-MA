import logging
from scapy.all import sniff, ARP, Ether, IP, TCP, UDP, Raw
from test import get_protocol_code, get_protocol_name

# Configure logging
logging.basicConfig(
    filename="arp_requests.log",
    filemode="a",  # Append to the log file
    format="%(asctime)s - %(message)s",
    level=logging.INFO
)

def packet_callback(packet):
    try:
        # Check for ARP layer
        if packet.haslayer(ARP):
            arp_layer = packet[ARP]
            log_message = (
                f"ARP Packet: {packet.summary()} | "
                f"Source MAC: {arp_layer.hwsrc}, Source IP: {arp_layer.psrc} | "
                f"Destination MAC: {arp_layer.hwdst}, Destination IP: {arp_layer.pdst}"
            )
            
            # Log the ARP request to the file
            logging.info(log_message)
            
            # Print to console for feedback
            print(log_message)
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
        logging.error(f"Error processing packet: {e}")
        print(f"Error processing packet: {e}")

def main():
    # Set the interface to capture packets from (change as needed)
    interface = "Wi-Fi"  # Change to your network interface
    print(f"Capturing packets on interface: {interface}")
    
    # Start packet capture
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
