#demo of gui from gpt

import tkinter as tk
from tkinter import ttk

# Create main application window
root = tk.Tk()
root.title("NetShield - Network Monitoring Tool")
root.geometry("900x600")
root.configure(bg="#2d2d2d")

# Define a style for the application
style = ttk.Style()

# Set a theme (this ensures consistent widget appearance across platforms)
style.theme_use('clam')

# Configure custom styles for the widgets
style.configure("TLabel", foreground="white", background="#2d2d2d", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12), foreground="white", background="#4CAF50")
style.configure("TFrame", background="#2d2d2d")
style.configure("Treeview", background="#3a3a3a", fieldbackground="#3a3a3a", foreground="white", rowheight=25)
style.configure("Treeview.Heading", background="#4CAF50", foreground="white", font=("Helvetica", 12))

# Top menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Home", menu=file_menu)
menu_bar.add_cascade(label="Settings")
menu_bar.add_cascade(label="Logs")

# Main frame for content
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill="both", expand=True)

# Left panel for active devices
left_frame = ttk.Frame(main_frame)
left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

device_label = ttk.Label(left_frame, text="Active Devices", font=("Helvetica", 16, "bold"))
device_label.pack(anchor="w")

device_list = ttk.Treeview(left_frame, columns=("IP Address", "MAC Address"), show="headings", height=10)
device_list.heading("IP Address", text="IP Address")
device_list.heading("MAC Address", text="MAC Address")
device_list.pack(fill="both", expand=True)

# Center frame for ARP status
center_frame = ttk.Frame(main_frame, padding="10")
center_frame.grid(row=0, column=1, sticky="nsew")

arp_status_label = ttk.Label(center_frame, text="ARP Spoofing Status", font=("Helvetica", 16, "bold"))
arp_status_label.pack()

# Traffic light-style status
status_indicator = tk.Label(center_frame, text="Safe", bg="green", fg="white", font=("Helvetica", 18, "bold"), width=15, height=3)
status_indicator.pack(pady=10)

# Right panel for defense and traffic logs
right_frame = ttk.Frame(main_frame)
right_frame.grid(row=0, column=2, sticky="nsew", padx=(10, 0))

defend_button = ttk.Button(right_frame, text="Defend Now", style="TButton")
defend_button.pack(pady=20)

log_label = ttk.Label(right_frame, text="Traffic Logs", font=("Helvetica", 16, "bold"))
log_label.pack(anchor="w")

log_list = tk.Listbox(right_frame, height=10, bg="#3a3a3a", fg="white", font=("Helvetica", 12))
log_list.pack(fill="both", expand=True)

# Bottom panel for scan button
bottom_frame = ttk.Frame(root, padding="10")
bottom_frame.pack(fill="x")

scan_button = ttk.Button(bottom_frame, text="Scan Network", style="TButton")
scan_button.pack(pady=10)

# Adjust grid weights for responsiveness
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(2, weight=1)

# Start the application
root.mainloop()
