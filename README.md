# IP Address Validator using Python

A simple Python command-line application that validates whether a user-provided IP address is a valid IPv4 or IPv6 address using Python's built-in `ipaddress` module.

---

## 📌 Features

* Validates IPv4 addresses.
* Validates IPv6 addresses.
* Accepts user input from the command line.
* Handles invalid inputs gracefully using exception handling.
* Uses Python's built-in `ipaddress` module (no external dependencies required).

---

## 🛠️ Technologies Used

* Python 3
* `ipaddress` module

---

## 📂 Project Structure

```
IP-Address-Validator/
│
├── ip_validator.py
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed on your system.

### Clone the Repository

```bash
git clone https://github.com/your-username/IP-Address-Validator.git
cd IP-Address-Validator
```

### Run the Program

```bash
python ip_validator.py
```

---

## 💻 Code

```python
import ipaddress

ip = input("Enter IP: ")

try:
    ipaddress.ip_address(ip)
    print("Valid IP")
except ValueError:
    print("Invalid IP")
```

---

## 📖 Example Usage

### Valid IPv4 Address

```
Enter IP: 192.168.1.1
Valid IP
```

### Invalid IP Address

```
Enter IP: 256.10.1.1
Invalid IP
```

### Valid IPv6 Address

```
Enter IP: 2001:db8::1
Valid IP
```

---

## 🎯 What I Learned

* Understanding the structure of IPv4 and IPv6 addresses.
* Using Python's built-in `ipaddress` module.
* Handling user input in Python.
* Implementing exception handling using `try` and `except`.
* Building a simple command-line application.
* Improving debugging and problem-solving skills.

---

