import sys
target = sys.argv[1] if len(sys.argv)>1 else 'https://testphp.vulnweb.com'
import requests

url = input("Website URL dao (https://example.com): ")

try:
    r = requests.get(url, timeout=5)
    print(f"\n[OK] Site Live! Status Code: {r.status_code}")
    print(f"Server: {r.headers.get('Server', 'Unknown')}")
    if r.status_code == 200:
        print("=> Bug Bounty er jonno ready!")
except Exception as e:
    print(f"\n[DOWN] Site e problem: {e}")

