import sys
target = sys.argv[1] if len(sys.argv)>1 else 'https://testphp.vulnweb.com'
import requests, re
from urllib.parse import urljoin

domain = input("Domain dao: ").strip()
domain = domain.replace("https://","").replace("http://","").split("/")[0]
headers = {"User-Agent": "Mozilla/5.0"}

url = "https://" + domain
try:
    requests.get(url, headers=headers, timeout=8)
except:
    url = "http://" + domain

print("\nTARGET:", url)

print("\n[1] Subdomain...")
try:
    r = requests.get("https://api.hackertarget.com/hostsearch/?q=" + domain, headers=headers, timeout=20)
    subs = [l for l in r.text.splitlines() if l]
    print("Found:", len(subs))
    for s in subs[:5]:
        print(s)
except Exception as e:
    print("Error", e)
    subs = []

print("\n[2] Links...")
html = ""
links = []
gold = []
try:
    html = requests.get(url, headers=headers, timeout=30).text
    links = re.findall(r'href="([^"]+)"', html)
    gold = [l for l in links if "?" in l and "=" in l]
    print("Total links:", len(links), " GOLD:", len(gold))
    for g in gold[:10]:
        print("GOLD ->", urljoin(url, g)[:150])
except Exception as e:
    print("Fail", e)

print("\n[3] JS...")
if html:
    jss = re.findall(r'src="([^"]+\.js[^"]*)"', html)
    print("Found JS:", len(jss))
    for j in jss[:5]:
        print(urljoin(url, j)[:150])

print("\nDone! You are best!")
