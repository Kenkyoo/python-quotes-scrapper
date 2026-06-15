import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def quotes_scrapper(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    quotes = []
    
    for element in soup.find_all(['p', 'div', 'span', 'li', 'blockquote']):
        txt = element.get_text(strip=True)
        
        patron = r'["\'“”]([^"\'“”]{20,200})["\'“”]'
        
        get_quotes = re.findall(patron, txt)
        for q in get_quotes:
            if len(q) > 15:
                quote = q.strip()
                if quote not in quotes:
                    quotes.append(quote)
    
    return quotes

link = input("Link to page scrapper: ")
quotes = quotes_scrapper(link)

if quotes:
    print(f"\n✅ Encontradas {len(quotes)} citas:\n")
    for i, q in enumerate(quotes, 1):
        print(f"{i}. {q}\n")
    
    df = pd.DataFrame(quotes, columns=['Quote'])
    print("\n📊 DataFrame:")
    print(df.head())
    
    df.to_csv('quotes.csv', index=False, encoding='utf-8')
    print("\n✅ Guardado en 'quotes.csv'")
else:
    print("❌ No se encontraron citas entre comillas")
