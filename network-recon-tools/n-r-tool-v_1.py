from scapy.all import *
import subprocess

networks = {}
iface = "wlan0mon"

def extract_channel(packet):
    if packet.haslayer(Dot11Elt) and packet.type == 0 and packet.subtype == 8:
        for elt in packet.getlayer(Dot11Elt):
            if elt.ID == 3:
                return elt.info[0]
    return None

def extract_ip(packet):
    if packet.haslayer(IP):
        return packet[IP].src
    return "N/A"

def scan_packet(packet):
    if packet.haslayer(Dot11Beacon):
        bssid = packet[Dot11].addr2
        ssid = packet[Dot11Elt].info.decode() if packet[Dot11Elt].info else "Hidden"
        channel = extract_channel(packet)
        if bssid not in networks:
            networks[bssid] = {
                "SSID": ssid,
                "Channel": channel,
                "BSSID": bssid,
                "IP": "N/A"
            }
            print(f"Network found - SSID: {ssid}, BSSID: {bssid}, Channel: {channel}")
    elif packet.haslayer(Dot11) and packet.type == 2:
        bssid = packet[Dot11].addr3
        if bssid in networks:
            ip = extract_ip(packet)
            if ip != "N/A":
                networks[bssid]["IP"] = ip
                print(f"IP Address found for BSSID {bssid}: {ip}")

def set_channel(iface, channel):
    subprocess.call(["iwconfig", iface, "channel", str(channel)])

print("Scanning for networks. Press Ctrl+C to stop.")
try:
    for channel in range(1, 15):
        set_channel(iface, channel)
        print(f"Scanning on channel {channel}...")
        sniff(iface=iface, prn=scan_packet, timeout=2)
except KeyboardInterrupt:
    print("\nScan complete. Networks found:")
    for net in networks.values():
        print(f"SSID: {net['SSID']}, BSSID: {net['BSSID']}, Channel: {net['Channel']}, IP: {net['IP']}")
