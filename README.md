# 🔍 SecureLens-AI V4.1 — 12-in-1 Autonomous Security Scanner

<p align="center">
<b>Powered by Meta Llama 3.3 | Built for Termux + Android | Hackathon Ready</b>
<br>
<i>12 Autonomous Lenses that think, hunt, and report like a real Pentester.</i>
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/AI-Llama%203.3-purple?style=for-the-badge">
<img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20Android-black?style=for-the-badge">
<img src="https://img.shields.io/badge/Lenses-12-in-1-red?style=for-the-badge">
</p>

### 🚀 What is SecureLens?
SecureLens is NOT just a scanner. It's an autonomous AI agent with 12 different eyes (lenses) to find vulnerabilities before hackers do.

### 🧠 The 12 Lenses
| Lens | What it does |
| :--- | :--- |
| 🔎 Recon Lens | Subdomain + Tech Stack Detection |
| 🛡️ Header Lens | Missing Security Headers |
| 🔑 Secret Lens | API Keys, Passwords in JS |
| 📜 JS Lens | Hidden Endpoints in JS files |
| 🔗 Param Lens | Hidden Parameters |
| 💉 XSS Lens | Reflected XSS Detection |
| 💣 SQLi Lens | SQL Injection Hunting |
| 🕵️ Hunter Lens | Sensitive Files / Logs |
| 🛡️ Safety Lens | Phishing / Malware Check |
| 🌐 Link Lens | Broken Links & Crawling |
| 📄 Page Lens | Content Analysis |
| 📝 Report Lens | Auto JSON + HTML Report with FIX |

### ⚡ Quick Start in Termux
```bash
git clone https://github.com/ya5891028-netizen/SecureLens-AI.git
cd SecureLens-AI
pip install -r requirements.txt
python securelens.py --url https://example.com
