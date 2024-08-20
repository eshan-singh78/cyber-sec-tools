Here’s a `README.md` file for your script:

# Deauthentication Attack Simulation and Network Interface Utility

This script allows you to simulate a deauthentication attack (for authorized testing purposes) and provides a utility to list available network interfaces and display their details.

## Features

- **List Network Interfaces**: List all available network interfaces on your machine.
- **Show Interface Details**: Display detailed information about a specific network interface.
- **Send Deauthentication Packets**: Simulate a deauthentication attack on a target device.

## Requirements

- Python 3.x
- [`scapy`](https://pypi.org/project/scapy/) library

## Installation

1. Clone this repository or download the script.
2. Install the required dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. List All Network Interfaces

To list all available network interfaces on your machine, run:

```bash
sudo python3 script.py --list
```

### 2. Show Details for a Specific Interface

To display detailed information about a specific network interface, run:

```bash
sudo python3 script.py --show <interface>
```

Replace `<interface>` with the name of the network interface, such as `wlan0`.

### 3. Send Deauthentication Packets

To simulate a deauthentication attack, you need to provide the target MAC address, gateway MAC address, and the network interface to use.

```bash
sudo python3 script.py <target_mac> <gateway_mac> <interface> --count 100
```

- `<target_mac>`: The MAC address of the target device.
- `<gateway_mac>`: The MAC address of the gateway (access point).
- `<interface>`: The network interface (e.g., `wlan0`).
- `--count`: (Optional) Number of deauthentication packets to send. Default is `100`.

**Example:**

```bash
sudo python3 script.py 00:11:22:33:44:55 66:77:88:99:AA:BB wlan0 --count 100
```

## Notes

- This script requires root privileges to send raw network packets. Use `sudo` when running it.
- Deauthentication attacks are illegal without permission. **Use this script only in authorized testing environments**.
- `iwconfig` is used to gather detailed information about network interfaces. Ensure it is installed on your system.

## Disclaimer

This tool is for educational and testing purposes only. Unauthorized use of deauthentication attacks is illegal and unethical. Use it responsibly and only in environments where you have explicit permission.
