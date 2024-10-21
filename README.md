# Internet Security & Malware Analysis Mini Project

Problem Statement: 
To Design and Implement a Network Monitoring Tool with ARP Spoofing Detection and Defense Mechanisms

Objectives:
Design and develop a python based tool capable of scanning local area networks and detecting active devices.
Monitor and detect ARP spoofing attacks.
Develop real-time defense mechanisms against ARP spoofing to safeguard network integrity.
Develop a user-friendly custom GUI for simplifying the process of traffic analysis, logging, and reporting.

Overview:
The Address Resolution Protocol (ARP) is an essential part of TCP/IP, responsible for mapping IP addresses to MAC addresses within a Local Area Network. This enables devices to communicate with each other through the Data Link Layer, enabling transfer of packets.
ARP Spoofing is a known vulnerability where an attacker can send falsified ARP messages to associate their MAC address with the IP address of another device, thus leading to Man in the MIddle or Denial of Service attacks.
Most operating systems lack built-in spoofing detection capabilities, leaving networks vulnerable to potential attacks.
Corporate networks, Public Wi-Fi networks and educational institutions are often vulnerable to ARP spoofing attacks.
This creates the need for a tool that can detect and prevent ARP spoofing in real-time, monitor network traffic and identify suspicious activities and mitigate attacks by restoring the correct ARP table entries without disrupting network communication.

Proposed System:
The proposed system will be built in python, primarily using Scapy, Tkinter and nmap. It will be divided into the following modules.

Network Scanning Module
Spoofing Detection Module
Spoofing Defense Module
Traffic Monitoring and Logging Module
GUI Module

Conclusion:
This project will demonstrate practical network monitoring, security, and defense mechanisms, providing hands-on experience with ARP-related network vulnerabilities. The developed tool will be versatile, easy to use, and capable of detecting and mitigating ARP spoofing attacks. By integrating real-time scanning, detection, and defense, the project will offer a comprehensive solution to a common network security problem.
