import sys
target = sys.argv[1] if len(sys.argv)>1 else 'https://testphp.vulnweb.com'
import requests, re

url = input("Website URL dao: ").strip()
if not url.startswith("http"):
    url = "http://" + url  # https na, http dilam

headers = {"User-Agent": "Mozilla/5.0"}

try:
    r = requests.get(url, headers=headers, timeout=20)
    print(f"\nConnected! Status: {r.status_code}\n")
    
    links = re.findall(r'href="([^"]+)"', r.text)
    found = 0
    for link in links:
        if "?" in link and "=" in link:
            print(link)
            found += 1
            if found >= 20:
                break
    if found == 0:
        print("Parameter link pai nai.")
    else:
        print(f"\nTotal {found} ta pelam.")

except Exception as e:
    print(f"\nError: {e}")
    print("Tip: Mobile data/WiFi check koro, ar Termux ke internet permission dao.")
