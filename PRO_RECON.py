import sys
target = sys.argv[1] if len(sys.argv)>1 else 'https://testphp.vulnweb.com'
import requests, re
from urllib.parse import urljoin

domain = input("Domain dao (ex: wikipedia.org): ").strip()
url = "https://" + domain.replace("https://","").replace("http://","").split("/")[0]

print(f"\n[*] Target: {url}\n")

# 1. Subdomain
print("[1] Subdomain khujchi...")
try:
    r = requests.get(f"https://api.hackertarget.com/hostsearch/?q={domain}", headers={"User-Agent":"Mozilla/5.0"}, timeout=15)
    subs = r.text.splitlines()
    print(f"  -> {len(subs)} ta pelam")
    for s in subs[:10]: print("   ", s)
except: print("  -> Fail")

# 2. Link & JS
print("\n[2] Link & JS khujchi...")
try:
    html = requests.get(url, headers={"User-Agent":"Mozilla/5.0"}, timeout=15).text
    links = re.findall(r'href="([^"]+)"', html)
    js = re.findall(r'src="([^"]+\.js[^"]*)"', html) + re.findall(r'src="([^"]*load\.php[^"]*)"', html)
    print(f"  -> {len(links)} ta link, {len(js)} ta JS")
    for l in links[:5]: print("   Link:", l[:80])
    for j in js[:5]: print("   JS:", j[:80])
    
    # report save
    with open("report.txt","w") as f:
        f.write(f"Target: {url}\n\nSubdomains:\n" + "\n".join(subs) + "\n\nLinks:\n" + "\n".join(links[:100]) + "\n\nJS:\n" + "\n".join(js))
    print("\n[✓] report.txt save holo!")
except Exception as e:
    print(f"Error: {e}")
