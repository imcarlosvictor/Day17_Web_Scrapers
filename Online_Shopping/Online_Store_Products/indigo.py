from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.chapters.indigo.ca/en-ca/home/search/?keywords=Programming#internal=1')
print(f'STATUS: [{source.status_code}]') # Print Status Code

soup = BeautifulSoup(source.text, 'lxml')
pretty_soup = soup.prettify()

product_container = soup.find_all(class_='product-list__product-list__product-container')
product_title = soup.find_all(class_='product-list__product-title-link--grid')
product_author = soup.find_all(class_='product-list__author-link product-list__contributor')

# Find product details
product_details = soup.find_all(class_='product-list__details-left')

# Prices
product_price_regular = soup.find_all(class_='')
product_price_sale = soup.find_all(class_='product-list__price--orange product-list__price--grid')


print(product_title)

# FIX: bs cannot find class... Returns None