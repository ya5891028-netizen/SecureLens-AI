import sys
target = sys.argv[1] if len(sys.argv)>1 else 'https://testphp.vulnweb.com'
import requests
import socket

print("[*] Bug Hunter Level 3 - Subdomain Finder\n")

domain = input("Domain de (ex: testfire.net): ")
if domain == "":
    domain = "testfire.net"

# Pro ra je common subdomain gula diye khuje
wordlist = [
    "www", "mail", "ftp", "admin", "test", "dev", "api",
    "blog", "shop", "vpn", "m", "portal", "secure",
    "beta", "staging", "demo", "app", "webmail", "ns1", "smtp"
]

print(f"\n[*] Scanning {len(wordlist)} subdomains for {domain}...\n")

found_subs = []

for sub in wordlist:
    full = f"{sub}.{domain}"
    try:
        # DNS check - eta diye bujhbo subdomain ta exist kore kina
        ip = socket.gethostbyname(full)
        print(f"  [FOUND] {full} -> {ip}")
        found_subs.append(full)
    except:
        print(f"  [NOT FOUND] {full}")

# Report save
with open("subdomains.txt", "w") as f:
    for s in found_subs:
        f.write(s + "\n")

print(f"\n[+] Done! {len(found_subs)} live subdomain found!")
print("[+] Saved to subdomains.txt")
print("Check: cat subdomains.txt")
