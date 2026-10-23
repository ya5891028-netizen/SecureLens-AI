import sys
target = sys.argv[1] if len(sys.argv)>1 else 'https://testphp.vulnweb.com'
import requests, re

url = input("JS link dao: ").strip()
headers = {"User-Agent": "Mozilla/5.0"}
r = requests.get(url, headers=headers, timeout=20)

print(f"File size: {len(r.text)} characters")

# Quote chara o khujbe, tai 0 asbe na
links1 = re.findall(r'https?://[^\s"\'<>]+', r.text)
links2 = re.findall(r'/[a-zA-Z0-9/_-]{4,}', r.text)

all_links = set(links1 + links2)
print(f"\n--- Pailam Total {len(all_links)} ta ---\n")
for l in sorted(all_links)[:40]:
    print(l)
