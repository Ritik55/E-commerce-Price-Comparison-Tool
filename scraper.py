import requests
from bs4 import BeautifulSoup
import pandas as pd

class EcommerceScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def scrape_amazon(self, product_name):
        url = f"https://www.amazon.com/s?k={product_name.replace(' ', '+')}"
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        products = []
        for item in soup.select('.s-result-item'):
            title = item.select_one('.a-text-normal')
            price = item.select_one('.a-price-whole')
            if title and price:
                products.append({
                    'title': title.text.strip(),
                    'price': float(price.text.replace(',', '')),
                    'source': 'Amazon'
                })
        return products

    def scrape_ebay(self, product_name):
        url = f"https://www.ebay.com/sch/i.html?_nkw={product_name.replace(' ', '+')}"
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        products = []
        for item in soup.select('.s-item'):
            title = item.select_one('.s-item__title')
            price = item.select_one('.s-item__price')
            if title and price:
                products.append({
                    'title': title.text.strip(),
                    'price': float(price.text.replace('$', '').replace(',', '')),
                    'source': 'eBay'
                })
        return products

    def scrape_all(self, product_name):
        amazon_products = self.scrape_amazon(product_name)
        ebay_products = self.scrape_ebay(product_name)
        return amazon_products + ebay_products
