import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def quotes_scrapper(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    quotes = []
    patron = r'["\'""]([^"\'""]{20,200})["\'""]'

    for element in soup.find_all(['p', 'div', 'span', 'li', 'blockquote']):
        txt = element.get_text(strip=True)
        for q in re.findall(patron, txt):
            if len(q) > 15:
                quote = q.strip()
                if quote not in quotes:
                    quotes.append(quote)

    return quotes
