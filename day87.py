#web crawler
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

visited = set()

def is_same_domain(start_url, link):
    return urlparse(start_url).netloc == urlparse(link).netloc

def crawl(url, depth=2):
    if depth == 0 or url in visited:
        return
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return

        visited.add(url)
        print(f"[+] Crawled: {url}")

        soup = BeautifulSoup(response.text, 'html.parser')
        for a_tag in soup.find_all('a', href=True):
            next_url = urljoin(url, a_tag['href'])
            if is_same_domain(url, next_url) and next_url not in visited:
                crawl(next_url, depth - 1)

        time.sleep(1)  # Be polite
    except Exception as e:
        print(f"[-] Failed to crawl {url}: {e}")

# 🔧 Start crawling
start_url = "https://example.com"
crawl(start_url, depth=2)
