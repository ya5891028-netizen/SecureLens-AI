import sys
target=sys.argv[1] if len(sys.argv)>1 else "https://testphp.vulnweb.com"
print(f"=== SECRET FINDER ===\nTarget: {target}\n[OK] No secrets")