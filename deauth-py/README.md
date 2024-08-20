# Network Interface Utility and Deauthentication Attack Simulation

This Python script allows you to manage network interfaces, scan for nearby wireless networks, and perform deauthentication attacks. It includes interactive options for selecting interfaces and scanning networks to perform authorized testing.

## Features

- **List Network Interfaces**: Lists all available network interfaces on the system.
- **Scan Wireless Networks**: Scans for available wireless networks on a selected interface.
- **Setup and Perform Deauthentication Attack**: Interactively guides you through selecting a network interface, scanning for networks, and performing a deauthentication attack.

## Requirements

- Python 3.x
- [`scapy`](https://pypi.org/project/scapy/)
- `iwconfig` and `iwlist` (tools for wireless network management, available on Linux)

## Installation

1. Clone the repository or download the script.
2. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have `iwconfig` and `iwlist` installed (these are typically included with the `wireless-tools` package on Linux). To install them:

   ```bash
   sudo apt-get install wireless-tools
   ```

## Usage

Run the script with `sudo`, as root privileges are required for network interface operations and sending raw packets.

### 1. List All Network Interfaces

To list all available network interfaces on your system, use:

```bash
sudo python3 script.py --list
```

This will display the network interfaces available for wireless operations, such as `wlan0`.

### 2. Scan Wireless Networks

To scan for nearby wireless networks on a specific interface, use the following command:

```bash
sudo python3 script.py --scan
```

You will be prompted to select a network interface, and the script will scan for available wireless networks, displaying their ESSID and MAC addresses.

### 3. Setup and Perform a Deauthentication Attack

To perform a deauthentication attack, use:

```bash
sudo python3 script.py --attack
```

During the attack setup, you will be guided through:
- Selecting the interface to use.
- Scanning for nearby networks.
- Inputting the target MAC address and the gateway (access point) MAC address.
- Setting the number of deauthentication packets to send (default is 100).

**Example:**

```bash
sudo python3 script.py --attack
```

You will select the interface, choose the target and gateway MAC addresses, and set the attack parameters interactively.

## Notes

- This script requires **root privileges** to scan networks and perform deauthentication attacks. Always run with `sudo`.
- **Deauthentication attacks are illegal** unless performed in an authorized testing environment. Only use this script for educational purposes or in scenarios where you have explicit permission.
- The script uses `iwconfig` and `iwlist` to scan wireless networks, so it will only work on systems where these tools are available (e.g., Linux).

## Disclaimer

This tool is designed for **educational purposes** and should only be used in controlled environments where you have permission to test network security. Unauthorized use of this tool for malicious purposes is illegal and unethical.
