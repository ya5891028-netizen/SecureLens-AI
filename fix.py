import os, glob
for file in glob.glob("*.py"):
    if file in ["securelens.py", "fix.py"]: continue
    try:
        with open(file, "r") as f: code = f.read()
        if "testfire.net" in code or "sys.argv" not in code:
            # Auto patch
            new_code = "import sys\ntarget = sys.argv[1] if len(sys.argv)>1 else 'https://testphp.vulnweb.com'\n" + code.replace('http://testfire.net', 'target').replace('https://testfire.net', 'target').replace('"testfire.net"', 'target')
            # Simple fix: just ensure target from argv
            if "target =" not in code:
                pass
            print(f"Fixing {file}...")
            # Better: prepend argv logic if missing
            if "sys.argv" not in code:
                with open(file, "r") as f: old = f.read()
                with open(file, "w") as f: f.write("import sys\ntarget = sys.argv[1] if len(sys.argv)>1 else 'https://testphp.vulnweb.com'\n" + old)
    except: pass
print("Done!")
