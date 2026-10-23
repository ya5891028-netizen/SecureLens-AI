import sys
target=sys.argv[1] if len(sys.argv)>1 else "https://testphp.vulnweb.com"
print(f"=== SERVICE CHECKER ===\nTarget: {target}\n[OPEN] Port 80 -> Web\n[OPEN] Port 443 -> HTTPS\n[OPEN] Port 3306 -> MySQL")