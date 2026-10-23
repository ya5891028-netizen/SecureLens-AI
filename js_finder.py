import sys
target = sys.argv[1] if len(sys.argv)>1 else 'https://testphp.vulnweb.com'
import requests, re

url = input("URL dao: ").strip()
if not url.startswith("http"): url = "https://" + url
headers = {"User-Agent": "Mozilla/5.0"}

r = requests.get(url, headers=headers, timeout=20).text

# 2 rokom pattern khujbe
js1 = re.findall(r'src="([^"]+\.js[^"]*)"', r)
js2 = re.findall(r'src="([^"]*load\.php[^"]*)"', r)

all_js = js1 + js2

print(f"\n{len(all_js)} ta JS file:\n")
for js in all_js[:20]:
    if js.startswith("/"):
        # purno link banano
        from urllib.parse import urljoin
        js = urljoin(url, js)
    print(js)
