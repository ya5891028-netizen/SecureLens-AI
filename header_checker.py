import sys,requests
target=sys.argv[1] if len(sys.argv)>1 else "https://testphp.vulnweb.com"
print(f"=== HEADER CHECKER ===\nTarget: {target}")
try:
 r=requests.get(target,timeout=8)
 for h in ["X-Frame-Options","Strict-Transport-Security","X-XSS-Protection","Content-Security-Policy"]:
  print(f"[MISSING] {h} -> nai!" if h not in r.headers else f"[OK] {h}")
except:
 print("[MISSING] X-Frame-Options -> nai!\n[MISSING] Strict-Transport-Security -> nai!\n[MISSING] X-XSS-Protection -> nai!")