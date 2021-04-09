from bs4 import BeautifulSoup
import requests
from typing import List

# Source
url = 'https://www.google.com/finance'

source = requests.get(url)

# Display Status Code
status = source.status_code
print(f'STATUS CODE: {status}')

soup = BeautifulSoup(source.text, 'lxml')

# def find_stock(*posistion: List[int]) -> str:

#     stock_block = soup.find_all(class_='QE2JIe')
#     company_name = stock_block[posistion].find(class_='TwnKPb')
#     stock_symbol = stock_block[posistion].find(class_='COaKTb')
#     following = stock_block[posistion].find(class_='Iap8Fc')
#     percent_change = stock_block[posistion].find(class_='JwB6zf')

#     return f'{company_name} ({stock_symbol}): {percent_change}'

def find_stock(*position: int) -> str:

    for num in position:
        stock_block = soup.find_all(class_='QE2JIe')
        company_name = stock_block[num].find(class_='TwnKPb')
        stock_symbol = stock_block[num].find(class_='COaKTb')
        # user_following = stock_block[posistion].find(class_='Iap8Fc')
        percent_change = stock_block[num].find(class_='JwB6zf')

        print(f'{company_name.get_text()} ({stock_symbol.get_text()}): {percent_change.get_text()}')

find_stock(0,1,2,3,4,5)