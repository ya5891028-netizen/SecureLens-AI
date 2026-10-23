import sys
target = sys.argv[1] if len(sys.argv)>1 else 'https://testphp.vulnweb.com'
import requests
from datetime import datetime

target = input("Target URL (https://example.com): ").strip()
if not target.startswith("http"):
    target = "https://" + target
target = target.rstrip("/")

paths = ["/admin", "/login", "/dashboard", "/api", "/backup", "/.env", "/config", "/test", "/robots.txt", "/sitemap.xml", "/admin/login", "/wp-admin"]

print(f"\n[~] Checking {target}\n")

found = []

for p in paths:
    full_url = target + p
    try:
        r = requests.get(full_url, timeout=5)
        status = r.status_code
        print(f"[{status}] {full_url}")
        if status in [200, 301, 302, 403]:
            found.append(f"[{status}] {full_url}")
    except:
        print(f"[ERROR] {full_url}")

# Save to file
filename = "result.txt"
with open(filename, "w") as f:
    f.write(f"Target: {target}\n")
    f.write(f"Time: {datetime.now()}\n")
    f.write("-"*40 + "\n")
    for item in found:
        f.write(item + "\n")

print(f"\n[OK] {len(found)} ta interesting link paisi!")
print(f"[SAVED] Result save hoise -> {filename} file e")
print("Dekhte chaile likho: cat result.txt")

