import os
import subprocess
 
def change_mac(interface, new_mac):
    try:
        print(f"Changing MAC address of {interface} to {new_mac}")
 
        # Bring the interface down
        subprocess.call(["sudo", "ifconfig", interface, "down"])
 
        # Change the MAC address
        subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
 
        # Bring the interface back up
        subprocess.call(["sudo", "ifconfig", interface, "up"])
 
        print(f"MAC address successfully changed to {new_mac}")
    except Exception as e:
        print(f"Error: {e}")
 
# Specify the interface and the spoofed MAC address
interface = "eth0"  # Replace with your network interface name
spoofed_mac = "00:aa:22:bb:44:cc"  # Replace with your desired MAC address
 
# Execute the MAC address change
change_mac(interface, spoofed_mac)