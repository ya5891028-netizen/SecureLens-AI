import sys
target = sys.argv[1] if len(sys.argv)>1 else 'https://testphp.vulnweb.com'
import requests, urllib3
urllib3.disable_warnings()
print("=== Level 4 - Asset Checker ===")
target = input("Target (only test site you own): ").strip()
if not target.startswith("http"): target = "http://" + target
target = target.rstrip("/")
wordlist = ["admin","login","robots.txt","sitemap.xml","api"]
headers = {"User-Agent":"Mozilla/5.0"}
print(f"\nChecking: {target}\n")
for w in wordlist:
    url = f"{target}/{w}"
    try:
        r = requests.get(url, headers=headers, timeout=15, verify=False, allow_redirects=True)
        print(f"[{r.status_code}] {url}")
    except Exception as e:
        print(f"[ERR] {url} -> {e}")
