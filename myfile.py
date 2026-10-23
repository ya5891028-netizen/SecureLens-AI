import sys
target = sys.argv[1] if len(sys.argv)>1 else 'https://testphp.vulnweb.com'
# site_map_viewer.py - Level 9 Final
import requests

print("=== SITE MAP VIEWER - LEVEL 9 ===")
domain = "testfire.net"
print(f"Target: {domain}")

# Eta crt.sh er bodole onno public API, eita te 429/502 ase na
url = f"https://api.hackertarget.com/hostsearch/?q={domain}"

headers = {"User-Agent": "Mozilla/5.0"}

try:
    r = requests.get(url, headers=headers, timeout=10)
    print(f"Status: {r.status_code}")
    print("\n--- Result ---")
    print(r.text[:2000])  # prothom 2000 word dekhabe

    lines = r.text.strip().split('\n')
    print(f"\n[OK] Total host pelam: {len(lines)} ta")
    
except Exception as e:
    print(f"[ERROR] {e}")
