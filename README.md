# WIFI-Scanner
This Python script was developed as part of learning the fundamentals of network security. It uses the Scapy library to capture wireless network traffic and discover available Wi-Fi networks (SSIDs) in the vicinity.

The script is designed to capture and analyze Beacon Frames—which broadcast network identity—by running the network card in Monitor Mode.

⚙️ How It Works
Packet Capture: The script listens to the specified wireless interface.

Filtering: It filters the captured packets to include only the Dot11Beacon frames (which announce network ID).

Information Extraction: It extracts the Network Name (SSID) and the BSSID (MAC Address) from each Beacon frame.

Unique Listing: It lists the detected networks without duplication and prints them to the console.

⚠️ Prerequisites and Requirements
For this script to function correctly, a Linux-based operating system (e.g., Kali Linux) and Root (Sudo) access are required.

Network Card: A wireless network adapter that supports Monitor Mode (e.g., cards with Realtek RTL8812AU chipsets) is necessary.

Scapy Installation: Install the required Python library:

Bash

pip install scapy
🚀 Usage Steps (For Kali Linux)
Switch Interface to Monitor Mode: (Assuming your interface name is wlan0)

Bash

sudo airmon-ng start wlan0
Note: This command will give you a new interface name, such as wlan0mon. Update the iface parameter in your code with this new name.

Run the Script:

Bash

sudo python3 wifi_scanner.py
Superuser permissions are required to start packet capturing.

To Revert to Normal Mode When Done:

Bash

sudo airmon-ng stop wlan0mon
🎯 Cybersecurity Focus
This tool serves as a fundamental application for developing Passive Network Reconnaissance skills and understanding the basic operating principles of wireless network cards.
