import sys
target = sys.argv[1] if len(sys.argv)>1 else 'https://testphp.vulnweb.com'
import requests, re

url = input("Website URL dao: ").strip()
if not url.startswith("http"):
    url = "https://" + url

headers = {"User-Agent": "Mozilla/5.0"}

try:
    r = requests.get(url, headers=headers, timeout=20)
    print(f"\n[✓] Connected: {r.status_code}\n")
    text = r.text

    links = re.findall(r'href="([^"]+)"', text)
    print(f"--- [1] Total {len(links)} ta link pelam ---")
    for l in links[:10]:
        print(l)

    print(f"\n--- [2] Parameter wala link (tomar 4 tar moto) ---")
    params = [l for l in links if "?" in l and "=" in l]
    if params:
        for p in params[:20]:
            print(p)
    else:
        print("Kono parameter nai, site ta clean.")

    print(f"\n--- [3] Secret Check ---")
    secrets = re.findall(r'(api_key|secret|password|token)\s*[:=]\s*["\']?([a-zA-Z0-9_\-]{8,})', text, re.I)
    if secrets:
        for s in secrets:
            print(f"Found: {s[0]}")
    else:
        print("Kono secret key pai nai. Valo!")

    print("\n--- Scan Ses ---")
    print("Note: Eta sudhu nijer site ba permission ache emon site e use korba.")

except Exception as e:
    print(f"Error: {e}")
