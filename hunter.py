import sys
target = sys.argv[1] if len(sys.argv)>1 else 'https://testphp.vulnweb.com'
import requests

target = input("Target URL (https://example.com): ").strip()
if not target.startswith("http"):
    target = "https://" + target
target = target.rstrip("/")

paths = ["/admin", "/login", "/dashboard", "/api", "/backup", "/.env", "/config", "/test"]

print(f"\n[~] Checking {target}\n")

for p in paths:
    full_url = target + p
    try:
        r = requests.get(full_url, timeout=5)
        if r.status_code == 200:
            print(f"[FOUND 200] {full_url}")
        elif r.status_code == 403:
            print(f"[FORBIDDEN 403] {full_url} -> Interesting!")
        elif r.status_code == 401:
            print(f"[AUTH 401] {full_url}")
        else:
            print(f"[{r.status_code}] {full_url}")
    except:
        print(f"[ERROR] {full_url}")

print("\n[~] Done! 200 / 403 gula bug bounty te important.")
