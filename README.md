# IPGuard

IPGuard is a simple tool for managing a list of blocked IP addresses. It allows you to block malicious IP addresses for a specified duration and automatically removes the IPs from the block list once the duration expires.

This library can be used in Flask or Django ( better to use in a middleware ).

## Features

- Add IP to block list with specified duration
- Remove IP from block list
- Check if an IP is currently blocked
- Manage block list using a JSON file

## Installation

1. Ensure you have Python 3.x and the required libraries (datetime, os, json, dateutil) installed on your system.
2. Download or clone the project files.

```bash
git clone https://github.com/yourusername/IPGuard.git
cd IPGuard
```

## Requirements

- first install *dateutil* lib with command bellow :
```bash
pip install python-dateutil
```

## Usage

```python
from IpGuardCore import IPGuard

# Create an instance of the IPGuard class
ip_guard = IPGuard()
int(ip_guard.IsBan("192.168.1.20"))

# Block an IP for a specified duration
ip_guard.Ban("192.168.1.20", year=0, month=0, day=15)

# Check again if the IP is blocked
print(ip_guard.IsBan("192.168.1.20"))

# Unblock the IP
ip_guard.UnBan("192.168.1.20")

# Check if the IP is still blocked
print(ip_guard.IsBan("192.168.1.20"))
```
