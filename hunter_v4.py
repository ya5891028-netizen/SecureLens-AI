import sys
target=sys.argv[1] if len(sys.argv)>1 else "https://testphp.vulnweb.com"
print(f"=== HUNTER V4 ===\nTarget: {target}\n[FOUND] {target} is live")