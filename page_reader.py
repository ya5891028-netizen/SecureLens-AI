import sys,requests
target=sys.argv[1] if len(sys.argv)>1 else "https://testphp.vulnweb.com"
print(f"=== PAGE READER ===\nTarget: {target}")
try:
 r=requests.get(target,timeout=8)
 print(f"Page length {len(r.text)}")
except Exception as e:
 print(f"Error {e}")
