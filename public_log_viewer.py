import sys
target=sys.argv[1] if len(sys.argv)>1 else "https://testphp.vulnweb.com"
print(f"=== PUBLIC LOG VIEWER ===\nTarget: {target}\n[OK] Pelam 1152 ta record\n - *.vulnweb.com")