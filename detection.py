import subprocess
import time

# Predefined trusted MAC addresses for critical devices
trusted_devices = {
    "192.168.22.102 ": "10:68:38:b1:84:81 ",  # Router's IP and MAC
    "192.168.22.85": "08:00:27:9d:4f:3a"  # Second machine's IP and MAC
}

# Function to run a shell command and capture its output
def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        return result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        print(f"[ERROR] Command failed: {command}")
        print(f"[ERROR] {e}")
        return "", str(e)

def get_arp_cache():
    """
    Retrieve the ARP cache table from the system using 'arp -n'.
    Returns a dictionary mapping IP addresses to lists of MAC addresses.
    """
    command = "arp -n"
    output, _ = run_command(command)  # Use the run_command function
    arp_cache = {}

    # Parse the output
    for line in output.splitlines()[1:]:  # Skip the header line
        parts = line.split()
        if len(parts) >= 3:
            ip_address = parts[0]
            mac_address = parts[2]
            # Add to the dictionary; allow for multiple MACs per IP
            if ip_address not in arp_cache:
                arp_cache[ip_address] = []
            arp_cache[ip_address].append(mac_address)

    return arp_cache


def validate_arp_entry(ip_address, current_mac):
    # Skip validation if IP and MAC match the trusted list
    if ip_address in trusted_devices and trusted_devices[ip_address] == current_mac:
        print(f"[INFO] Trusted entry detected: {ip_address} -> {current_mac}")
        return True

    # Validate MAC via arping
    command = f"arping -c 1 {ip_address}"
    output, _ = run_command(command)
    for line in output.splitlines():
        if "reply from" in line:
            validated_mac = line.split()[-1].strip("[]")
            return validated_mac == current_mac
    return False

def restore_arp_entry(ip_address, mac_address):
    """
    Restore the correct ARP entry for a given IP and MAC address in the actual ARP table.
    """
    print(f"[INFO] Restoring ARP entry for {ip_address} -> {mac_address}")
    # Add the correct ARP entry to the system's ARP cache
    run_command(f"arp -s {ip_address} {mac_address}")
    print(f"[INFO] Restored ARP entry: {ip_address} -> {mac_address}")

def process_arp_cache():
    arp_cache = get_arp_cache()
    for ip, mac_list in arp_cache.items():
        print(f"[DEBUG] Processing IP: {ip}, MAC List: {mac_list}")
        if len(mac_list) > 1:
            print(f"[WARNING] Multiple MAC addresses detected for IP: {ip}")
            for mac in mac_list:
                if not validate_arp_entry(ip, mac):
                    print(f"[SPOOFED] Detected spoofed entry for IP: {ip}, MAC: {mac}")
                    run_command(f"arp -d {ip}")  # Remove spoofed entry
                    # Restore the original MAC address from the trusted devices dictionary
                    if ip in trusted_devices:
                        restore_arp_entry(ip, trusted_devices[ip])
        else:
            mac = mac_list[0]
            if not validate_arp_entry(ip, mac):
                print(f"[SPOOFED] Detected spoofed entry for IP: {ip}, MAC: {mac}")
                run_command(f"arp -d {ip}")  # Remove spoofed entry
                # Restore the original MAC address from the trusted devices dictionary
                if ip in trusted_devices:
                    restore_arp_entry(ip, trusted_devices[ip])
            else:
                print(f"[VALID] IP: {ip}, MAC: {mac}")

# Main function to drive the program
def main():
    print("[INFO] Starting ARP spoofing detection...")
    try:
        while True:
            process_arp_cache()  # Call to process the ARP cache
            time.sleep(5)  # Adjust the sleep time as needed (e.g., every 5 seconds)
    except KeyboardInterrupt:
        print("\n[INFO] Program terminated.")

if __name__ == "__main__":
    main()
