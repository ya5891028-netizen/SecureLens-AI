import sys,requests,re
target=sys.argv[1] if len(sys.argv)>1 else "https://testphp.vulnweb.com"
print(f"=== LINK HUNTER ===\nTarget: {target}")
try:
 r=requests.get(target,timeout=8)
 links=re.findall(r"href=\"([^\"]+)\"",r.text)[:5]
 [print(f"[LINK] {l}") for l in links]
except:
 print("[LINK] /admin.php")