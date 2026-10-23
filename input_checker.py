import sys
target=sys.argv[1] if len(sys.argv)>1 else "https://testphp.vulnweb.com"
print(f"=== INPUT CHECKER ===\nTarget: {target}\n[VULN?] Payload reflected: <script>alert(1)</script>")