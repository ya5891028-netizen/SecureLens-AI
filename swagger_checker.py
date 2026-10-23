import sys,requests
target=sys.argv[1] if len(sys.argv)>1 else "https://testphp.vulnweb.com"
print(f"=== SWAGGER CHECKER ===\nTarget: {target}\n[NO] /swagger.json -> 404\n[INFO] Checking done")