import sys
target = sys.argv[1] if len(sys.argv)>1 else 'https://testphp.vulnweb.com'
import requests

domain = input("Domain dao (wikipedia.org): ").strip()
url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
headers = {"User-Agent": "Mozilla/5.0"}

try:
    r = requests.get(url, headers=headers, timeout=15)
    print(r.text)
    lines = r.text.splitlines()
    print(f"\n[✓] {len(lines)} ta subdomain pelam:\n")
    for line in lines[:30]:
        print(line)
except Exception as e:
    print(f"Error: {e}")
