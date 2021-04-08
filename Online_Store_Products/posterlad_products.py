from bs4 import BeautifulSoup
import requests

# Get URL
url = requests.get('https://posterlad.com/')
soup = BeautifulSoup(url.text, 'html.parser')
print(f'RESPONSE: [{url.status_code}]')  # Print status code

# Grabs all info
product_name = soup.find_all(class_='grid-product__title')
product_price_GBP = soup.find_all(class_='money')
# product_price_USD = soup.find_all(attrs={'doubly-currency': 'USD'})
product_link = soup.find_all()


product = zip(product_name, product_price_GBP)
product = list(product)

for name, price in product:
    print(f'Name: {name.text}, Price: {price.text}')