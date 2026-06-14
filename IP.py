import ipaddress

ip = input("Enter IP: ")

try:
    ipaddress.ip_address(ip)
    print("Valid IP")
except ValueError:
    print("Invalid IP")