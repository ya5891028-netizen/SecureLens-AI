import sys
target = sys.argv[1] if len(sys.argv)>1 else 'https://testphp.vulnweb.com'
import requests, re
url = input("Website URL dao: ").strip()
if not url.startswith("http"):
    url = "https://" + url

headers = {"User-Agent": "Mozilla/5.0"}
r = requests.get(url, headers=headers, timeout=15)

# 2 rokom vabe link khujbo
links1 = re.findall(r'href="([^"]+)"', r.text, re.I)
links2 = re.findall(r'https?://[^\s"\'<>]+', r.text)
all_links = links1 + links2

uniq = list(set(all_links))
print(f"\nTotal {len(uniq)} ta link pawa geche:\n")
for l in uniq[:30]:
    print(l)
