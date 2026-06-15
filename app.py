import requests
from bs4 import BeautifulSoup

link = 'https://quotes.toscrape.com/'
res = requests.get(link)
soup = BeautifulSoup(res.text, 'html.parser')

quotes = []

for quote in soup.find_all('span', class_='text'):
    quotes.append(quote.text[1:-1])
    print(quote.text[1:-1], "\n")
