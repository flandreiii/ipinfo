# 🔍 ipinfo — Network Recon Tool

> Created by **flandreiii** | For educational & authorized penetration testing only

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20CachyOS%20%7C%20Kali-red?style=for-the-badge&logo=linux)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Author](https://img.shields.io/badge/Author-flandreiii-purple?style=for-the-badge)](https://buymeacoffee.com/flandreiii)

---

## ☕ Support the Creator

If you find this tool useful, consider buying me a coffee!

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-flandreiii-yellow?style=for-the-badge&logo=buy-me-a-coffee)](https://buymeacoffee.com/flandreiii)

👉 **https://buymeacoffee.com/flandreiii**

---

## 📖 Description

**ipinfo** is a powerful network reconnaissance tool built for security researchers and penetration testers. It combines IP geolocation, port scanning, OS detection, and Metasploit payload references into one clean interactive CLI tool.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🌍 **IP & Geo Info** | Country, city, region, ISP, ASN, hostname |
| 🔓 **Port Scanning** | Top 1000 ports with service & version detection |
| 💻 **OS Detection** | Fingerprint the target's operating system |
| 🛠️ **Metasploit Examples** | Ready-to-use msfvenom payload references |
| 🎨 **Colored Output** | Clean, color-coded terminal interface |
| 📋 **Interactive Menu** | Easy-to-use numbered selection menu |

---

## 📦 Installation

### 🤖 Termux
```bash
pkg update && pkg upgrade
pkg install python nmap
chmod +x ipinfo.py
```

### 🐧 CachyOS
```bash
sudo pacman -Syu
sudo pacman -S python nmap
chmod +x ipinfo.py
```

### 🔴 Kali Linux
```bash
sudo apt update && sudo apt upgrade
sudo apt install python3 nmap
chmod +x ipinfo.py
```

---

## 🚀 Usage

```bash
# Interactive menu
python3 ipinfo.py <IP>

# One-shot flags
python3 ipinfo.py <IP> --geo      # IP + Geolocation info
python3 ipinfo.py <IP> --ports    # Port scan
sudo python3 ipinfo.py <IP> --os  # OS detection (root required)
python3 ipinfo.py <IP> --msf      # Metasploit payload examples
python3 ipinfo.py <IP> --all      # Run everything
```

### Example
```bash
python3 ipinfo.py 8.8.8.8
```

---

## 🖥️ Preview

```
  ██╗██████╗ ██╗███╗   ██╗███████╗ ██████╗
  ██║██╔══██╗██║████╗  ██║██╔════╝██╔═══██╗
  ██║██████╔╝██║██╔██╗ ██║█████╗  ██║   ██║
  ██║██╔═══╝ ██║██║╚██╗██║██╔══╝  ██║   ██║
  ██║██║     ██║██║ ╚████║██║     ╚██████╔╝
  ╚═╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝
         Network Recon Tool
         Creator: flandreiii

──────────── MENU ────────────
  [1] IP / Geo Location Info
  [2] Port Scan
  [3] OS Detection
  [4] Metasploit Payload Examples
  [5] Run All
  [0] Exit
──────────────────────────────

  ipinfo >
```

---

## ⚠️ Disclaimer

> This tool is intended **strictly for educational purposes** and **authorized penetration testing only**.
> 
> - ✅ Only use on systems you **own** or have **explicit written permission** to test.
> - ❌ Unauthorized scanning or exploitation is **illegal** and punishable by law.
> - The creator (**flandreiii**) holds **no responsibility** for any misuse of this tool.

---

## 🧰 Requirements

- Python 3.x
- nmap
- Internet connection (for geo lookup)
- Root/sudo (for OS detection only)

---

## 📄 License

MIT License — free to use, modify, and distribute with credit.

---

## 🔗 Connect

| Platform | Link |
|---|---|
| ☕ Buy Me a Coffee | [buymeacoffee.com/flandreiii](https://buymeacoffee.com/flandreiii) |

---

#hacking #cybersecurity #penetrationtesting #nmap #metasploit #kalilinux #termux #cachyos #infosec #ethicalhacking #networksecurity #recon #python #opensource #bugbounty #redteam #security #linux #pentest #flandreiii
