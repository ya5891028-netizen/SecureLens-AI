import sys
target = sys.argv[1] if len(sys.argv)>1 else 'https://testphp.vulnweb.com'
import requests

domain = input("Domain dao (wikipedia.org): ").strip()
url = f"https://crt.sh/?q=%.{domain}&output=json"
try:
    r = requests.get(url, timeout=20)
    subs = set()
    for entry in r.json():
        subs.add(entry['name_value'])
    print(f"\n[✓] {len(subs)} ta subdomain pelam:\n")
    for s in list(subs)[:30]:
        print(s)
except Exception as e:
    print(f"Error: {e} - crt.sh block korse, VPN diye try koro")
