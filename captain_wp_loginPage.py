import requests
import threading
from fake_useragent import UserAgent

# Common WordPress login paths
wp_paths = [
    "wp-admin", "wp-login.php", "admin", "login", "wp/wp-admin",
    "cms/wp-admin", "wordpress/wp-admin", "blog/wp-admin"
]

def check_wp_login(target_url, path):
    """Check if a given WordPress login page exists."""
    url = f"{target_url.rstrip('/')}/{path}"
    headers = {"User-Agent": UserAgent().random}  # Random user-agent for each request

    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            print(f"[+] Found: {url}")
        else:
            print(f"[-] Not found: {url}")
    except requests.exceptions.RequestException:
        print(f"[!] Error checking: {url}")

def start_scan(target_url):
    """Run scans using multi-threading for faster execution."""
    threads = []
    for path in wp_paths:
        thread = threading.Thread(target=check_wp_login, args=(target_url, path))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    target = input("Enter target website (e.g., https://example.com): ")
    start_scan(target)