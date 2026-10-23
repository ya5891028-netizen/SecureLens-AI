import sys,requests
target=sys.argv[1] if len(sys.argv)>1 else "https://testphp.vulnweb.com"
print(f"=== PAGE CHECKER ===\nTarget: {target}")
for p in ["/admin","/login","/api","/.env"]:
 try:
  r=requests.get(target.rstrip("/")+p,timeout=5)
  print(f"[FOUND] {p} -> {r.status_code}")
 except:
  print(f"[NO] {p}")