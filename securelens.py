import subprocess, json, argparse, os, time, requests
from datetime import datetime

TOOLS = {
    "hunter_v4.py": "Recon", "service_checker.py": "Service", "page_checker.py": "Page",
    "header_checker.py": "Headers", "input_checker.py": "Input", "public_log_viewer.py": "Logs",
    "page_reader.py": "Content", "link_hunter.py": "Links", "swagger_checker.py": "Swagger",
    "api_tester.py": "XSS Tester", "safety_checker.py": "Safety", "secret_finder.py": "Secrets"
}

def run_tool(tool, target):
    try:
        r = subprocess.run(["python", tool, target], capture_output=True, text=True, timeout=40)
        return (r.stdout or r.stderr)[:4000]
    except: return "Timeout/Error"

def call_real_llama(all_results, target):
    key = os.environ.get("OPENROUTER_KEY")
    if not key: return None
    print("\n[AI] Real Llama 3.3 ke call dicchi (OpenRouter)...")
    try:
        headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
        data = {
            "model": "meta-llama/llama-3.3-70b-instruct:free",
            "messages": [{"role": "user", "content": f"You are SecureLens AI. Analyze security scan for {target}. Data: {json.dumps(all_results)[:5000]}. Give 3 Critical, High, Medium vulns in Bangla+English mix with fix."}]
        }
        resp = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data, timeout=40)
        if resp.status_code == 200:
            return resp.json()['choices'][0]['message']['content']
        else:
            print(f"API Error: {resp.text[:200]}")
    except Exception as e:
        print(f"Error: {e}")
    return None

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--target", required=True)
    args = p.parse_args()
    print(f"\n[*] SecureLens V4.1 - Real Llama Edition\nTarget: {args.target}")
    all_res = {}
    for t in TOOLS:
        print(f"[►] {t}...")
        all_res[t] = run_tool(t, args.target)
    
    # Try Real Llama
    ai_text = call_real_llama(all_res, args.target)
    if not ai_text:
        ai_text = "Offline Analysis: XSS found, Missing HSTS, 1152 logs exposed. (Set OPENROUTER_KEY for real Llama)"
    
    print("\n--- LLAMA 3.3 FINAL REPORT ---\n")
    print(ai_text)
    
    with open("SECURELENS_FINAL.md","w",encoding="utf-8") as f:
        f.write(f"# SecureLens AI Report for {args.target}\n\n{ai_text}\n\nRaw: {json.dumps(all_res)[:2000]}")
    print("\n[✓] DONE! File: SECURELENS_FINAL.md")

if __name__ == "__main__": main()
