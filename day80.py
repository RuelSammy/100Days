#script to scrape bbc.com
import requests
from bs4 import BeautifulSoup

# BBC News URL
url = 'https://www.bbc.com/news'

# Set a user-agent to avoid 403 errors
headers = {
    'User-Agent': 'Mozilla/5.0'
}

# Send request
response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find headline elements
    headlines = soup.find_all('h2', class_='sc-5r1tcc-5')  # This may change over time

    print("BBC News Headlines:\n")
    for idx, h in enumerate(headlines, 1):
        text = h.get_text(strip=True)
        print(f"{idx}. {text}")
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")

with open('bbc_headlines.txt', 'w', encoding='utf-8') as f:
    for idx, h in enumerate(headlines, 1):
        text = h.get_text(strip=True)
        f.write(f"{idx}. {text}\n")
